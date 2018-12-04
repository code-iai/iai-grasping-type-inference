from grasping_type_inference.inference import Inference


def test_should_return_the_most_probable_result():
    inference = Inference(':LEFT-SIDE', ':BOTTOM', 'cup.n.01')
    result = inference.get_most_probable_result()

    assert 'grasp_type(LEFT-SIDE)' == result