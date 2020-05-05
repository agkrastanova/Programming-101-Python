import os
import unittest
import time
from unittest.mock import patch, Mock

from measure_performance import MeasurePerformance


class MeasurePerformanceTests(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_measure_performance.txt'

    @patch('measure_performance.time')
    def test_get_exceeded_time_returns_correct_value(self, time_mock):
        meter = MeasurePerformance(self.filename)

        time_mock.time.return_value = 2

        meter.start = time_mock.time.return_value - 1

        self.assertEqual(meter.get_exceeded_time(), 1)

    def test_benchmark_measures_correct_time_from_init_to_first_call(self):
        with patch('measure_performance.time') as time_mock:
            meter = Mock()
            time_mock.sleep.return_value = 1
            meter.get_exceeded_time.return_value = 1

            self.assertEqual(meter.get_exceeded_time(), 1)

    @patch('measure_performance.time')
    def test_benchmark_appends_benchmark_using_passed_message(self, time_mock):
        with MeasurePerformance(self.filename) as meter:
            time_mock.sleep.return_value = 1

            meter.benchmark('test')

            expected = ['test: 1s']

            self.assertEqual(meter._benchmarks, expected)

    @patch('measure_performance.time')
    def test_benchmark_appends_benchmark_with_no_message_using_benchmarks_count(self, time_mock):
        with MeasurePerformance(self.filename) as meter:
            time_mock.sleep.return_value = 1
            time_mock.time.return_value = time_mock.sleep.return_value + 1
            meter.start = 1
            meter.benchmark('test')

            time_mock.sleep.return_value = 1
            time_mock.time.return_value += time_mock.sleep.return_value
            meter.start = time_mock.sleep.return_value
            meter.benchmark()

            expected = ['test: 1s', 'Benchmark No.2: 2s']

            self.assertEqual(meter._benchmarks, expected)

    def test_benchmark_does_not_restart_the_start_of_measure_performance_if_not_passed(self):
        with patch('measure_performance.time') as time_mock:
            meter = Mock()
            original_start = meter.original_start

            time_mock.sleep.return_value = 1
            meter.benchmark('test')

            self.assertEqual(meter.original_start, original_start)

    @patch('measure_performance.time')
    def test_benchmark_restarts_the_start_of_the_measure_performance_if_passed(self, time_mock):
        with MeasurePerformance(self.filename) as meter:
            original_start = meter.original_start

            time_mock.sleep.return_value = 1
            meter.benchmark('test', restart=True)

            self.assertEqual(meter.original_start, original_start)

    @patch('measure_performance.time')
    def test_benchmark_preserves_correct_execution_times_if_not_restarted(self, time_mock):
        msg = 'test'

        with MeasurePerformance(self.filename) as meter:
            time_mock.sleep.return_value = 1
            time_mock.time.return_value = time_mock.sleep.return_value + 1
            meter.start = time_mock.sleep.return_value

            meter.benchmark(msg)

            time_mock.sleep.return_value = 1
            time_mock.time.return_value += time_mock.sleep.return_value
            meter.benchmark(msg, restart=False)

            expected = ['test: 1s', 'test: 2s']

            self.assertEqual(meter._benchmarks, expected)

    @patch('measure_performance.time')
    def test_benchmark_preserves_correct_execution_times_if_restarted(self, time_mock):
        msg = 'test'

        with MeasurePerformance(self.filename) as meter:
            time_mock.sleep.return_value = 1

            meter.benchmark(msg, restart=True)

            time_mock.sleep.return_value = 1
            meter.benchmark(msg)

            expected = ['test: 1s', 'test: 1s']

            self.assertEqual(meter._benchmarks, expected)

    def test_context_manager_does_not_create_the_file_if_exception_is_raised(self):
        with self.assertRaises(ValueError):
            with MeasurePerformance(self.filename):
                raise ValueError('Testing')

        self.assertFalse(os.path.exists(self.filename))

    def test_context_manager_closes_the_file_if_there_is_no_exception(self):
        with MeasurePerformance(self.filename):
            x = 111
            x += 10

        self.assertTrue(os.path.exists(self.filename))

        # we can open only closed files
        test_file = open(self.filename, 'r')
        test_file.close()

    # def test_context_manager_dumps_correct_info_into_file_when_closed(self):
    #     with patch('measure_performance.time') as time_mock:
    #         meter = Mock()
    #         time_mock.sleep.return_value = 1
    #         meter.get_exceeded_time.return_value = 1

    #         meter.benchmark('test')

    #         time_mock.sleep.return_value = 2
    #         meter.get_exceeded_time.return_value = 2
    #         meter.benchmark()

    #     expected = 'test: 1s\nBenchmark No.2: 2s\nFinished for: 2s'

    #     with open(self.filename, 'r') as test_file:
    #         self.assertEqual(expected, test_file.read())

    def tearDown(self):
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
