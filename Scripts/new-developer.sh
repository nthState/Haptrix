echo "Let's get started..."


echo "Do you want to enable auto-signing your commits?"
echo "Will use key `id_ed25519`"
echo "Remember to upload your signing key to GitHub"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) git config --global gpg.format ssh; git config --global user.signingkey ~/.ssh/id_ed25519.pub; git config --global commit.gpgsign true; break;;
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