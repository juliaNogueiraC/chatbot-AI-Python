{pkgs}: {
  deps = [
    pkgs.python311Packages.pillow-simd
    pkgs.run
    pkgs.python311Packages.tkinter
  ];
}
