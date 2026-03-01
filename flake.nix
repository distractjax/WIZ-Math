{
  description = "A basic python dev flake";

  # Inputs: where to get packages from
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";
  };

  outputs = { self, nixpkgs }:
    let
      # Define the systems you want to support
      allSystems = [
        "x86_64-linux" #64-bit Intel/AMD Linux
        "aarch64-darwin" # Apple Silicon Mac
      ];

      forAllSystems = f: nixpkgs.lib.genAttrs allSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      devShells = forAllSystems ({ pkgs }: {
        default = pkgs.mkShell {
          # Packages to include in the environment
          packages = with pkgs; [
            (python3.withPackages (ps: with ps; [
              debugpy
              pandas
							pytest
            ]))
            basedpyright
            ruff
            markdownlint-cli
            # Add more project-specific packages here
          ];
          # Shell commands to run upon activation
          shellHook = ''
            						echo "Entering the development environment..."
            					'';
        };
      });
    };
}
