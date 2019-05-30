import file_helper

def test_testdir():
    """

    :return:
    """
    filelist = file_helper.listDir("test_dir")
    assert (filelist == ['file2.txt', 'file1.txt'])