from backend import model as m, runtime as r
from datetime import datetime, date
from dataclasses import replace
import sqlite3
import pytest
from os import path

class TestHandleCommand:
    initial_state = m.GlobalState()
    
    def test_save_to_db(self):
        test_sub_state = {
            'start_time': datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S.%f"),
            'end_time': datetime.strftime(datetime(2027, 11, 8),"%Y-%m-%d %H:%M:%S.%f"),
            'question_type': 'Test Type',
            'question_module': 'Test Module',
            'is_answer_correct': True,
        }

        start_time = datetime.strptime(test_sub_state['start_time'], "%Y-%m-%d %H:%M:%S.%f") 
        end_time = datetime.strptime(test_sub_state['end_time'], "%Y-%m-%d %H:%M:%S.%f") 
        exec_time = end_time - start_time
        app_path = path.expanduser('~/.local/share/gre-prep/test/')

        test_state = replace(
            self.initial_state,
            app_path = app_path,
            db_path = path.join(app_path, 'gre_prep.db'),
            sub_state = test_sub_state,
        )

        cmd = m.Cmd.SAVE_TO_DB
        new_state = r.handle_command(test_state, cmd)

        conn = sqlite3.connect(new_state.db_path)

        try:
            with conn:
                c = conn.cursor()
                c.execute('SELECT * FROM problem_history WHERE exec_time = (SELECT MAX(exec_time) FROM problem_history);')
                test_data = c.fetchone()
        finally:
            conn.close()

        assert new_state == test_state
        assert test_data[0] == test_sub_state['start_time']
        assert test_data[1] == test_sub_state['question_type']
        assert test_data[2] == test_sub_state['question_module']
        assert test_data[3] == test_sub_state['is_answer_correct']
        assert test_data[4] == exec_time.total_seconds()


class TestMsgFactory:
    def test_other_target(self):
        json_dump = {
            'target': 'Math Server',
            'message': 'TEST',
            'payload': {
                'view_type': None,
                'problem_history': None,
            }
        }

        msg = r.msg_factory(json_dump)

        assert msg == m.QueriedSubstate(message = json_dump['message'], payload = json_dump['payload'])
