from setuptools import find_packages,setup


HYPEN_E_DOT="-e ."
def get_req(file_path):
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject1',
    version='0.0.1',
    author='Darshan',
    author_email='DarshanKumarr03@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt'))