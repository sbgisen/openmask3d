#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2024 SoftBank Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json
import pathlib

import numpy as np

if __name__ == '__main__':
    video_path = pathlib.Path('dataset') / 'video'
    for image in (video_path / 'color').glob('*.jpg'):
        i = image.stem.split('-')[0]
        image.rename(image.parent / f'{int(i)}.jpg')
    for image in (video_path / 'depth').glob('*.png'):
        i = image.stem.split('-')[0]
        image.rename(image.parent / f'{int(i)}.png')
    for image in (video_path / 'poses').glob('*.txt'):
        i = image.stem.split('-')[0]
        image.rename(image.parent / f'{int(i)}.txt')
    (video_path / 'poses').rename(video_path / 'pose')
    with open(video_path / 'config.json', 'r') as f:
        config = json.load(f)
        intrinsic = np.eye(4)
        intrinsic[0, 0] = config['cam_intr'][0][0]
        intrinsic[1, 1] = config['cam_intr'][1][1]
        intrinsic[0, 2] = config['cam_intr'][0][2]
        intrinsic[1, 2] = config['cam_intr'][1][2]
        intrinsic_path = video_path / 'intrinsic'
        intrinsic_path.mkdir(exist_ok=True)
        with open(intrinsic_path / 'intrinsic_color.txt', 'w') as f:
            np.savetxt(f, intrinsic)
