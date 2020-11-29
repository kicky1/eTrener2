import os
from os.path import dirname, abspath

import tensorflow as tf



from tf_pose.network_cmu import CmuNetwork



def _get_base_path():
    if not os.environ.get('OPENPOSE_MODEL', ''):
        return './models'
    return os.environ.get('OPENPOSE_MODEL')


def get_network(type, placeholder_input, sess_for_load=None, trainable=True):
    if type in ['cmu', 'openpose']:
        net = CmuNetwork({'image': placeholder_input}, trainable=trainable)
        pretrain_path = 'numpy/openpose_coco.npy'
        last_layer = 'Mconv7_stage6_L{aux}'
    elif type in ['cmu', 'cmu_q']:
        net = CmuNetwork({'image': placeholder_input}, trainable=trainable)
        last_layer = 'Mconv7_stage6_L{aux}'
    else:
        raise Exception('Invalid Model Name.')

    pretrain_path_full = os.path.join(_get_base_path(), pretrain_path)
    if sess_for_load is not None:
        if type in ['cmu', 'vgg', 'openpose']:
            if not os.path.isfile(pretrain_path_full):
                raise Exception('Model file doesn\'t exist, path=%s' % pretrain_path_full)
            net.load(os.path.join(_get_base_path(), pretrain_path), sess_for_load)
    return net, pretrain_path_full, last_layer


def get_graph_path(model_name):
    dyn_graph_path = {
        'cmu': 'graph/cmu/graph_opt.pb',
    }

    base_data_dir = dirname(dirname(abspath(__file__)))
    if os.path.exists(os.path.join(base_data_dir, 'models')):
        base_data_dir = os.path.join(base_data_dir, 'models')
    else:
        base_data_dir = os.path.join(base_data_dir, 'tf_pose_data')

    graph_path = os.path.join(base_data_dir, dyn_graph_path[model_name])
    if os.path.isfile(graph_path):
        return graph_path

    raise Exception('Plik grafu nie istnieje, path=%s' % graph_path)


def model_wh(resolution_str):
    width, height = map(int, resolution_str.split('x'))
    if width % 16 != 0 or height % 16 != 0:
        raise Exception('Wysokosc i szerkosc musza byc wielokrotnoscia liczby 16. w=%d, h=%d' % (width, height))
    return int(width), int(height)
