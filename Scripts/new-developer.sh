echo "Let's get started installing dependencies..."


echo "Do you want to clone the repo?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) git clone git@github.com:nthState/HaptrixShared.git; break;;
        No ) break;;
    esac
done


echo "Do you want to install xcode command line tools?"
echo "Generally if you have Xcode these are already installed"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) xcode-select --install; break;;
        No ) break;;
    esac
done


echo "Do you want to install Homebrew?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"; break;;
        No ) break;;
    esac
done


echo "Do you want to install SwiftLint?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) brew install swiftlint; break;;
        No ) break;;
    esac
done


#https://commitizen-tools.github.io/commitizen/
echo "Do you want to install Commitizen?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) brew install commitizen; break;;
        No ) break;;
    esac
done


#https://pre-commit.com/
echo "Do you want to install pre-commit?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) brew install pre-commit; break;;
        No ) break;;
    esac
done


echo "Do you want to configure pre-commit?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) pre-commit install --hook-type commit-msg --hook-type pre-push; pre-commit autoupdate; break;;
        No ) break;;
    esac
done