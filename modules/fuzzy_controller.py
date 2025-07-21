# Fuzzy logic controller
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
lane_status = ctrl.Antecedent(np.arange(0, 3, 1), 'lane_status')  # 0 = no lanes, 1 = partial, 2 = good
threshold_change = ctrl.Consequent(np.arange(-20, 21, 1), 'threshold_change')

# Membership functions for lane_status
lane_status['missing'] = fuzz.trimf(lane_status.universe, [0, 0, 1])
lane_status['partial'] = fuzz.trimf(lane_status.universe, [0, 1, 2])
lane_status['good'] = fuzz.trimf(lane_status.universe, [1, 2, 2])

# Membership functions for threshold_change
threshold_change['decrease'] = fuzz.trimf(threshold_change.universe, [-20, -15, -5])
threshold_change['none'] = fuzz.trimf(threshold_change.universe, [-2, 0, 2])
threshold_change['increase'] = fuzz.trimf(threshold_change.universe, [5, 15, 20])

# Fuzzy rules
rule1 = ctrl.Rule(lane_status['missing'], threshold_change['decrease'])
rule2 = ctrl.Rule(lane_status['partial'], threshold_change['none'])
rule3 = ctrl.Rule(lane_status['good'], threshold_change['increase'])

threshold_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

def tune_threshold(fuzzy_params):
    threshold_simulator = ctrl.ControlSystemSimulation(threshold_ctrl)

    if fuzzy_params["left_detected"] and fuzzy_params["right_detected"]:
        lane_state = 2  # good
    elif fuzzy_params["left_detected"] or fuzzy_params["right_detected"]:
        lane_state = 1  # partial
    else:
        lane_state = 0  # missing

    threshold_simulator.input['lane_status'] = lane_state
    threshold_simulator.compute()

    delta = threshold_simulator.output['threshold_change']
    new_high = fuzzy_params["high_thresh"] + delta
    new_high = max(50, min(150, int(new_high)))

    return new_high
