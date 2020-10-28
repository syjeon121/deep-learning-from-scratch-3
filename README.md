『밑바닥부터 시작하는 딥러닝 ❸』
==========================
<p>
<a href="https://www.amazon.co.jp/dp/4873119065/ref=cm_sw_r_tw_dp_U_x_KiA1Eb39SW14Q"><img src="https://github.com/WegraLee/deep-learning-from-scratch-3/blob/master/cover.jpg" height="200" align=right></a>
</p>

## DeZero 빌드 현황

<p>
<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/dezero_logo.png" width="400px" </p>

<p>
  <a href="https://pypi.python.org/pypi/dezero"><img
		alt="pypi"
		src="https://img.shields.io/pypi/v/dezero.svg"></a>
  <a href="https://github.com/oreilly-japan/deep-learning-from-scratch-3/blob/master/LICENSE.md"><img
		alt="MIT License"
		src="http://img.shields.io/badge/license-MIT-blue.svg"></a>
  <a href="https://travis-ci.org/oreilly-japan/deep-learning-from-scratch-3"><img
		alt="Build Status"
		src="https://travis-ci.org/oreilly-japan/deep-learning-from-scratch-3.svg?branch=master"></a>
</p>


## 시리즈 소개

<a href="https://github.com/WegraLee/deep-learning-from-scratch-3/blob/master/%EB%B0%91%EB%B0%94%EB%8B%A5123.pdf"><img src="https://github.com/WegraLee/deep-learning-from-scratch-3/blob/master/%EB%B0%91%EB%B0%94%EB%8B%A5123.png" width=1000></a>

* [『밑바닥부터 시작하는 딥러닝』 깃허브 저장소](https://github.com/WegraLee/deep-learning-from-scratch)
* [『밑바닥부터 시작하는 딥러닝 ❷』 깃허브 저장소](https://github.com/WegraLee/deep-learning-from-scratch-2)

## 새소식

:white_check_mark: **2020.11.20** - 출간

:white_check_mark: **2020.10.18** - 베타리뷰 완료

## 소개

『밑바닥부터 시작하는 딥러닝 ❸』에서는 'DeZero'라는 이 책의 오리지널 딥러닝 프레임워크를 만듭니다. DeZero는 파이토치, 텐서플로 2.0, 체이너 같은 현대적인 프레임워크가 채택한 동적 계산 그래프(Define-by-Run) 방식의 프레임워크입니다. 최소한의 코드로, 하지만 충분히 강력한 프레임워크를 총 60단계에 걸쳐 완성합니다. 이를 통해 여러분은 다음과 같은 효과를 얻으실 수 있을 겁니다.
 
* 파이토치, 텐서플로 2.0 같은 현대적인 딥러닝 프레임워크의 동작 원리를 깨우친다.
* 현대적인 딥러닝 프레임워크를 떠받드는 기술과 사상을 들여다본다.
* 딥러닝을 한 차원 깊게 이해한다.
* ‘프레임워크’를 직접 개발해보는 경험을 쌓아, 개발자로서 한 단계 성장한다.
* 유용한 프로그래밍 관례를 익힌다.

더 자세한 소개 정보는 다음 문서를 참고하세요.
* *[상세 소개 및 목차](https://docs.google.com/document/d/1nJ9vhQnAnc3yW2OLFBFkv9NvKFuP0igGjgaz9ykCySo/)*

## 베타리뷰

한국어판 베타리뷰는 최대의 효과를 내기 위해 딥러닝 경력, 개발 경력, 학계/업계, 중검 검토 분야 등을 종합해 리뷰어 분들은 선정했습니다. 그리고 많은 분이 적극 참여해주셔서 기대 이상의 피드백을 받았습니다. 값진 시간 내어주신 모든 분께 감사드립니다.

[그림] 한국어판 베타리더 분포

<img src="https://github.com/WegraLee/deep-learning-from-scratch-3/blob/master/dezero_reviewers.png" width=1000>


## 파일 구성

|폴더 이름 |설명                         |
|:--        |:--                          |
|[dezero](/dezero)       |DeZero의 소스 코드 |
|[examples](/examples)      |Dezero를 사용한 구현 예    |
|[steps](/steps)|각 단계의 파일（step01.py ~ step60.py）|
|[tests](/tests)|DeZero 단위 테스트|


## 요구사항
소스 코드를 실행하려면 아래의 소프트웨어가 설치되어 있어야 합니다.

- [Python 3](https://docs.python.org/3/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

또한 선택사항으로 엔비디아 GPU에서 수행할 수 있는 기능도 제공합니다. 이 경우 다음 라이브러리가 필요합니다.

- [CuPy](https://cupy.chainer.org/) （선택사항）


## 실행방법

steps 폴더 안의 step01.py, step02.py, ... 파일들이 각 단계에서 작성한 파일에 해당합니다. 실행하려면 프로젝트 루트에서 다음의 python 명령어를 입력합니다.

```
$ python steps/step01.py
$ python steps/step02.py
```

다음과 같이 해당 단계의 디렉터리 안에서 실행할 수도 있습니다.

```
$ cd steps
$ python step31.py
```

## 데모
[examples](/examples) 디렉터리에서 DeZero의 다른 구현 예를 찾아볼 수 있습니다.

[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/example_tanh.png" height="175"/>](https://github.com/oreilly-japan/deep-learning-from-scratch-3/tree/tanh)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/example_spiral.png" height="175"/>](/examples/spiral.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/example_gpu.png" height="175"/>](https://colab.research.google.com/github/oreilly-japan/deep-learning-from-scratch-3/blob/master/examples/mnist_colab_gpu.ipynb)

[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/gan.gif" height="175"/>](/examples/gan.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/vae.png" height="175"/>](/examples/vae.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/grad_cam.png" height="175"/>](/examples/grad_cam.py)

[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/style_transfer.png" height="175"/>](/examples/style_transfer.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/pythonista.png" height="175"/>](https://github.com/oreilly-japan/deep-learning-from-scratch-3/wiki/DeZero%E3%82%92iPhone%E3%81%A7%E5%8B%95%E3%81%8B%E3%81%99)

## 책의 오류

이 책의 오탈자 등 오류 정보는 아래 정오표에서 확인하실 수 있습니다.

* [정오표](https://docs.google.com/document/d/1_qHrFCrfx5zNOdslAa9rY3Vv1KECLCToHWJNhvn2jDA)
