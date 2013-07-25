import argparse
import re
import os
import subprocess


class RunPylint(object):
    def run(self):
        args = self._parse_arguments()
        try:
            report = subprocess.check_output(['pylint', args.filename])
        except Exception as error:
            report = error.output
        if args.full_report:
            print report
            return
        code_rating = self._parse_for_code_rating(report)
        print 'Your Code Rating is {0}'.format(code_rating)

    def _parse_arguments(self):
        parser = argparse.ArgumentParser(description='Run Pylint against the file.')
        parser.add_argument('-f', '--filename', help='File against which PyLint will run.')
        parser.add_argument('-r', '--full_report', default=False, type=bool, help='To generate full pylint report.')
        args = parser.parse_args()
        return args
        
    def _parse_for_code_rating(self, report):
        regex = 'Your code has been rated at ([0-9]{1,2}\.[0-9]{1,2})\/.+'
        parsed_string = re.search(regex, report)
        return parsed_string.group(1)



if __name__ == '__main__':
    RunPylint().run()
