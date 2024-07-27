import importlib.util  # To dynamically import the problems package
import os


def main() -> None:
    problem_file_name = "Test"

    # Finding the path of the file
    problem_file_path = os.path.join(os.path.dirname(__file__), "..", "Problems", problem_file_name + ".py")

    # Create module specification
    problem_spec = importlib.util.spec_from_file_location(problem_file_path + "module", problem_file_path)

    # Create a Module Object
    problem_module = importlib.util.module_from_spec(problem_spec)

    # Load the module code
    problem_spec.loader.exec_module(problem_module)

    # Access the class from the loaded module
    problem_class = getattr(problem_module, problem_file_name)

    # Creating an object
    problem_object = problem_class()

    # Run the solution
    problem_object.run_solution()


if __name__ == "__main__":
    main()
