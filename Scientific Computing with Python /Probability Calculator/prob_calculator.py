import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):
    self.contents = [color for color, count in balls.items() for _ in range(count)]

  def draw(self, num_balls_drawn):
    if num_balls_drawn >= len(self.contents):
      return self.contents

    drawn_ball = random.sample(self.contents, num_balls_drawn)
    for balls in drawn_ball:
      self.contents.remove(balls)
    return drawn_ball

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    drawn_balls_dict = {x: drawn_balls.count(x) for x in drawn_balls}
    if all(drawn_balls_dict.get(color, 0) >= count for color, count in expected_balls.items()):
        success += 1
  return success / num_experiments
