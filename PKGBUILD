# Maintainer: Antoine Carpentier <antoine.carpentier.info@gmail.com>
pkgname=pointcarrefs
pkgver=r4.226c5bb
pkgrel=1
pkgdesc="Mount pointcarre.vub.ac.be with fuse"
arch=('any')
url="chaaaaateau.noip.me/shitgotreal/MagicToon.jpg"
license='GPL'
groups=()
depends=(fuse python2 python2-requests python2-beautifulsoup4 python2-pip)
makedepends=('git')
provides=("${pkgname%}")
conflicts=("${pkgname%}")
replaces=()
backup=()
options=(!emptydirs)
install=()
source=('pointcarrefs::git+https://github.com/titouanc/PointCarreFS')
noextract=()
md5sums=('SKIP')

pkgver() {
	cd "$srcdir/$pkgname"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
	cd "$srcdir/$pkgname"
	python2 setup.py install --optimize=1
}
