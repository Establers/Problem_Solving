# [Platinum V] 나이트의 경로 - 18137 

[문제 링크](https://www.acmicpc.net/problem/18137) 

### 성능 요약

메모리: 116320 KB, 시간: 188 ms

### 분류

애드 혹

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e9316526-e533-4485-8855-023296f9caf2/-/preview/"></p>

<p style="text-align: center;"><그림> 무한 격자에서의 나이트의 경로</p>

<p>오른쪽과 위쪽으로 무한히 많이 뻗어 나가는 격자판이 있다. 이 격자에서 왼쪽에서 x번째, 아래에서 y번째 칸에는 수 <mjx-container class="MathJax" jax="CHTML" display="true" style="font-size: 109%; position: relative;"><mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-mfrac><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-mrow><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-mrow></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mfrac><mrow><mo stretchy="false">(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo><mo stretchy="false">(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>−</mo><mn>2</mn><mo stretchy="false">)</mo></mrow><mn>2</mn></mfrac><mo>+</mo><mi>y</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$$\frac{(x+y-1)(x+y-2)}{2}+y$$</span></mjx-container>가 쓰여 있다. 이 방법을 사용하면, 각 칸을 하나의 양의 정수에 일대일 대응시킬 수 있다.</p>

<p>여기서 나이트(체스의 기물 중 하나)는 격자판을 이동하려고 한다. 나이트는 두 칸 전진 후, 전진한 방향에서 오른쪽 혹은 왼쪽 중 한 방향으로 한 칸을 이동한다. 전진하는 방향은 위쪽, 아래쪽, 오른쪽 혹은 왼쪽 중 아무 방향이어도 상관없다. 하지만 격자판을 나가서는 안 된다. 즉, 나이트가 격자판 바깥으로 나가는 경우가 없다고 할 때 8칸 중 하나로 이동할 수 있다. 하지만 가장 왼쪽 아래에 있는 칸인 1번 칸에서는 8번 칸이나 9번 칸 중 하나로밖에 이동할 수 없다.</p>

<p>나이트는 1번 칸에서 시작해서 k번 이동하려고 한다. 이동하는 과정에서 나이트가 이동할 수 있는 칸이 여럿 있을 수 있다. 그러면 나이트는 한 번도 방문하지 않은 칸을 방문하려고 한다. 한 번도 방문하지 않은 칸이 여러 개일 경우에는 그중 쓰인 수가 제일 작은 칸으로 이동하고, 한 번도 방문하지 않은 칸이 없을 때는 더 이동하지 않고 멈춘다.</p>

<p>나이트가 k번 이동한 후에 위치한 칸의 번호를 찾는 프로그램을 작성하여라.</p>

### 입력 

 <p>나이트가 이동하는 횟수인 음이 아닌 정수 k가 첫째 줄에 주어진다. k가 0일 수 있음에 유의하여라.</p>

<p>나이트가 k번 이동하는 동안 멈추지 않으며, 그동안 방문한 칸에는 모두 2<sup>31</sup> 미만의 정수가 쓰여 있는 k만 입력으로 주어짐이 보장된다.</p>

### 출력 

 <p>나이트가 k번 이동한 후에 위치한 칸의 번호를 출력하여라.</p>

