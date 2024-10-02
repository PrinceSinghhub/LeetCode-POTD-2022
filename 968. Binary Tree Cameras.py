import math
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def postorder(node):
            if not node:
                return (0, math.inf)

            l_count, l_state = postorder(node.left)
            r_count, r_state = postorder(node.right)

            state = min(l_state, r_state)
            total_cameras = l_count + r_count

            if state == 0:  # children are not monitored
                return (total_cameras + 1, 1)  # install camera in current node

            if state == 1:  # one of the children is monitored and has camera
                return (total_cameras, 2)  # set current node state as monitored but no camera

            return (total_cameras, 0)  # set current node as unmonitored

        # adding dummy parent for the root for handling cases where root need a camera
        dummy = TreeNode(-1, root)

        return postorder(dummy)[0]