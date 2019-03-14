import os

def train(solver_dir):
    solver_filenames = os.listdir(solver_dir)

    for solver in solver_filenames:
        pass
        print solver
        command = '/home/user01/caffe/build/tools/caffe train --gpu 5 --solver ' + solver
        os.system(command)
if __name__ == '__main__':
    solver_dir = 'single_solver/'
    train(solver_dir)