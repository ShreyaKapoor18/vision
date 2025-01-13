# import pytest
# from pytest import approx

# from brainscore_vision import score


# @pytest.mark.private_access
# @pytest.mark.memory_intense
# @pytest.mark.parametrize("model_identifier, benchmark_identifier, expected_score", [
#     ("ReAlnet01", "MajajHong2015.IT-pls", approx(0.51075, abs=0.0005)),
# ])
# def test_score(model_identifier, benchmark_identifier, expected_score):
#     actual_score = score(model_identifier=model_identifier, benchmark_identifier=benchmark_identifier,
#                          conda_active=True)
#     assert actual_score == expected_score


import pytest
import brainscore_vision


@pytest.mark.travis_slow
def test_has_identifier():
    model = brainscore_vision.load_model('ReAlnet01')
    assert model.identifier == 'ReAlnet01'