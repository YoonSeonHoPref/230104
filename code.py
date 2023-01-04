# 구글 코랩을 열어줍니다

# kaggle에서 자신의 account에 들어가서 
# API 카테고리에서 Create New API Token을 클릭해 kaggle.json 파일을 저장합니다.



!pip install kaggle

from google.colab import files
file.upload()

# json파일을 업로드 해줍니다


!mkdir -p ~/.kaggle               # Kaggle 폴더 생성 
!cp kaggle.json ~/.kaggle/        # Kaggle 폴더에 kaggle.json 파일 복사
!chmod 600 ~/.kaggle/kaggle.json  # 나에게만 읽기,쓰기 권한 
 

!kaggle competitions download -c dfl-bundesliga-data-shootout
# 캐글 데이터 다운 아래에서 복사 후 느낌표만 붙이면 됨 

!unzip /content/dfl-bundesliga-data-shootout.zip         # 압축 해제
!ls                                                      # 확인

# 끝




# 예외로 캐글 공유된 코드도 copy 버튼 누르고 옮겨적기해서 느낌표만 붙이면 바로 

!kaggle kernels pull its7171/yolov7-finetune-with-soccernet




