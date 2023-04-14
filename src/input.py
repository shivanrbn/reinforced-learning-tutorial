import numpy as np


class InputControls:
    """
    Handles and contains userinput
    """

    def pressed_to_action(self, keytouple):
        """
        # ─── KEY IDS ─────────
        # arrow forward   : 119 w
        # arrow backwards : 115 s
        # arrow left      : 97 a
        # arrow right     : 100 d
        """
        action_turn = 0.
        action_acc = 0.
        if keytouple[115] == 1:  # back
            action_acc -= 1
        if keytouple[119] == 1:  # forward
            action_acc += 1
        if keytouple[97] == 1:  # left  is -1
            action_turn += 1
        if keytouple[100] == 1:  # right is +1
            action_turn -= 1

        return np.array([action_acc, action_turn])
