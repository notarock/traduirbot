{ pkgs ? import <nixpkgs> { } }:

with pkgs;
(buildFHSUserEnv {
  name = "Traduirbot";
  targetPkgs = _: [
    stdenv.cc.cc.lib
    pipenv
    python38
  ];
}).env
