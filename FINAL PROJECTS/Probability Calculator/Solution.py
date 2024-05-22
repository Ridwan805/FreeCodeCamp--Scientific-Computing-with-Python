import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            temp = self.contents
            self.contents = []
            return temp
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        test_hat = copy.deepcopy(hat)
        drawn_balls = test_hat.draw(num_balls_drawn)

        success = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                success = False
                break
        if success:
            success_count += 1
    probability = success_count / num_experiments
    return probability

# Test case
hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat, expected_balls={"red": 1, "green": 2}, num_balls_drawn=4, num_experiments=2000)
print(f"Probability: {probability}")
