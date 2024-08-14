# QuantumComputer

## pip 基本操作

```bash

% 仮想環境作成 カレントディレクトリに作成される
python -m venv envname

% 仮想環境起動
envname\Scripts\activate

% 仮想環境終了
(envname)> deactivate

% pythonの場所確認
where python

% 環境を外部保存
pip freeze > requirements.txt

% requirementsから環境作成
python -m pip install -r requirements.txt
python -m pip install --proxy http://userID:Password@hg-vm-prx-sdc.t.rd.honda.com:8080 -r requirements.txt

```
