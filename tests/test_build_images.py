import pytest
from tests.build_image_base_test import BuildImageBase, AL2023BasedBuildImageBase


@pytest.mark.java8X86_64
class TestBIJava8(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java8", "Dockerfile-java8", "maven")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "1.8', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.java8_al2X86_64
class TestBIJava8AL2(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java8.al2", "Dockerfile-java8-al2", "gradle", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "1.8', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.java8_al2Arm64
class TestBIJava8AL2ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java8.al2", "Dockerfile-java8-al2", "gradle", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "1.8', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.java11X86_64
class TestBIJava11(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java11", "Dockerfile-java11", "maven", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "11.0.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.java11Arm64
class TestBIJava11ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java11", "Dockerfile-java11", "maven", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "11.0.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.java17X86_64
class TestBIJava17Maven(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java17", "Dockerfile-java17", "maven", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "17.0.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.java17Arm64
class TestBIJava17ForArmMaven(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java17", "Dockerfile-java17", "maven", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "17.0.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.java17X86_64
class TestBIJava17AL2Gradle(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java17", "Dockerfile-java17", "gradle", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "17.0', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.java17Arm64
class TestBIJava17AL2ForArmGradle(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java17", "Dockerfile-java17", "gradle", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "17.0', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("aarch64"))

@pytest.mark.java21X86_64
class TestBIJava21Maven(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java21", "Dockerfile-java21", "maven", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "21.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.java21Arm64
class TestBIJava21ForArmMaven(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java21", "Dockerfile-java21", "maven", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "21.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.java21X86_64
class TestBIJava21Gradle(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java21", "Dockerfile-java21", "gradle", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "21', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.java21Arm64
class TestBIJava21ForArmGradle(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java21", "Dockerfile-java21", "gradle", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "21', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.nodejs16xX86_64
class TestBINode16(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs16.x", "Dockerfile-nodejs16x", "npm", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v16."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.nodejs16xArm64
class TestBINode16ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs16.x", "Dockerfile-nodejs16x", "npm", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v16."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.nodejs18xX86_64
class TestBINode18(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs18.x", "Dockerfile-nodejs18x", "npm", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v18."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.nodejs18xArm64
class TestBINode18ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs18.x", "Dockerfile-nodejs18x", "npm", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v18."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("aarch64"))

@pytest.mark.nodejs20xX86_64
class TestBINode20(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs20.x", "Dockerfile-nodejs20x", "npm", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v20."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.nodejs20xArm64
class TestBINode20ForArm(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs20.x", "Dockerfile-nodejs20x", "npm", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v20."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.python37X86_64
class TestBIPython37(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.7", "Dockerfile-python37", "pip")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.7."))
        self.assertTrue(self.is_package_present("pip"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.python38X86_64
class TestBIPython38(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.8", "Dockerfile-python38", "pip", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.8."))
        self.assertTrue(self.is_package_present("pip"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.python38Arm64
class TestBIPython38ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.8", "Dockerfile-python38", "pip", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.8."))
        self.assertTrue(self.is_package_present("pip"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.python39X86_64
class TestBIPython39(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.9", "Dockerfile-python39", "pip", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.9."))
        self.assertTrue(self.is_package_present("pip"))


@pytest.mark.python310Arm64
class TestBIPython310ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.10", "Dockerfile-python310", "pip", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.10."))
        self.assertTrue(self.is_package_present("pip"))


@pytest.mark.python310X86_64
class TestBIPython310(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.10", "Dockerfile-python310", "pip", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.10."))
        self.assertTrue(self.is_package_present("pip"))

@pytest.mark.python311Arm64
class TestBIPython311ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.11", "Dockerfile-python311", "pip", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.11."))
        self.assertTrue(self.is_package_present("pip"))


@pytest.mark.python311X86_64
class TestBIPython311(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.11", "Dockerfile-python311", "pip", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.11."))
        self.assertTrue(self.is_package_present("pip"))

@pytest.mark.python312Arm64
class TestBIPython312ForArm(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.12", "Dockerfile-python312", "pip", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.12."))
        self.assertTrue(self.is_package_present("pip"))


@pytest.mark.python312X86_64
class TestBIPython312(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.12", "Dockerfile-python312", "pip", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.12."))
        self.assertTrue(self.is_package_present("pip"))


@pytest.mark.python39Arm64
class TestBIPython39ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.9", "Dockerfile-python39", "pip", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.9."))
        self.assertTrue(self.is_package_present("pip"))


@pytest.mark.dotnet6X86_64
class TestBIDotNet6(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            "dotnet6", "Dockerfile-dotnet6", tag="x86_64", dep_manager="cli-package"
        )

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "6"))
        self.assertTrue(self.is_package_present("dotnet"))


@pytest.mark.dotnet6Arm64
class TestBIDotNet6Arm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            "dotnet6", "Dockerfile-dotnet6", tag="arm64", dep_manager="cli-package"
        )

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "6"))
        self.assertTrue(self.is_package_present("dotnet"))


@pytest.mark.dotnet7X86_64
class TestBIDotNet7(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            "dotnet7", "Dockerfile-dotnet7", tag="x86_64", dep_manager="cli-package"
        )

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "7"))
        self.assertTrue(self.is_package_present("dotnet"))


@pytest.mark.dotnet7Arm64
class TestBIDotNet7Arm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            "dotnet7", "Dockerfile-dotnet7", tag="arm64", dep_manager="cli-package"
        )

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "7"))
        self.assertTrue(self.is_package_present("dotnet"))

# TODO (hawflau): Revert change after publishing preview image
@pytest.mark.dotnet8X86_64
def test_dummy():
    assert 1 == 1

@pytest.mark.dotnet8Arm64
def test_dummy_for_arm64():
    assert 1 == 1

@pytest.mark.ruby32X86_64
class TestBIRuby32(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("ruby3.2", "Dockerfile-ruby32", "bundler", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("ruby --version", "ruby 3.2."))
        self.assertTrue(self.is_package_present("bundler"))
        self.assertTrue(self.is_package_present("gem"))
        self.assertTrue(self.is_architecture("x86_64"))

@pytest.mark.ruby32Arm64
class TestBIRuby32ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("ruby3.2", "Dockerfile-ruby32", "bundler", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("ruby --version", "ruby 3.2."))
        self.assertTrue(self.is_package_present("bundler"))
        self.assertTrue(self.is_package_present("gem"))
        self.assertTrue(self.is_architecture("aarch64"))

@pytest.mark.go1xX86_64
class TestBIGo1(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("go1.x", "Dockerfile-go1x", "mod")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("go version", "go1."))
        self.assertTrue(self.is_package_present("go"))


@pytest.mark.providedX86_64
class TestBIProvided(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("provided", "Dockerfile-provided")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("go version", "go1."))
        self.assertTrue(self.is_package_present("go"))


@pytest.mark.provided_al2X86_64
class TestBIProvidedAL2(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("provided.al2", "Dockerfile-provided-al2", tag="x86_64")

    def test_architecture(self):
        """
        Test architecture of this build image
        """
        self.assertTrue(self.is_architecture("x86_64"))

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("go version", "go1."))
        self.assertTrue(self.is_package_present("go"))


@pytest.mark.provided_al2Arm64
class TestBIProvidedAL2ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("provided.al2", "Dockerfile-provided-al2", tag="arm64")

    def test_architecture(self):
        """
        Test architecture of this build image
        """
        self.assertTrue(self.is_architecture("aarch64"))

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("go version", "go1."))
        self.assertTrue(self.is_package_present("go"))


@pytest.mark.provided_al2023X86_64
class TestBIProvidedAL2023(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            "provided.al2023", "Dockerfile-provided-al2023", tag="x86_64"
        )

    def test_architecture(self):
        """
        Test architecture of this build image
        """
        self.assertTrue(self.is_architecture("x86_64"))

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("go version", "go1."))
        self.assertTrue(self.is_package_present("go"))


@pytest.mark.provided_al2023Arm64
class TestBIProvidedAL2023ForArm(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("provided.al2023", "Dockerfile-provided-al2023", tag="arm64")

    def test_architecture(self):
        """
        Test architecture of this build image
        """
        self.assertTrue(self.is_architecture("aarch64"))

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("go version", "go1."))
        self.assertTrue(self.is_package_present("go"))
