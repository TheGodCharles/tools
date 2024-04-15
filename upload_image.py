import io
import oss2

from PIL import Image


ACCESS_KEY_ID = ''
ACCESS_KEY_SECRET = ''
END_POINT = ''
BUCKET_NAME = ''
ALIYUN_OSS_CNAME = ''


def upload_to_oss(file_obj, oss_path, headers=None):
    auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
    bucket = oss2.Bucket(auth, f'http://{END_POINT}', BUCKET_NAME)

    if isinstance(file_obj, Image.Image):
        s = io.BytesIO()
        try:
            file_obj.save(s, 'jpeg')
        except:
            file_obj.save(s, 'png')
        s.seek(0)
        file_obj = s

    # 将文件对象定位到开头，以确保在上传前文件对象处于正确的读取位置
    if hasattr(file_obj, 'seek'):
        file_obj.seek(0)

    items = oss_path.split('?', 1)
    oss_path_real = items[0]

    result = bucket.put_object(oss_path_real, file_obj, headers)
    assert result.status == 200, result

    url = f'https://{ALIYUN_OSS_CNAME}/{oss_path}'
    return url


if __name__ == '__main__':
    file_obj = ''
    oss_path = ''
    url = upload_to_oss(file_obj, oss_path)