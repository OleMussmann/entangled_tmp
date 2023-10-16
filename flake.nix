{
  description = "my project description";

  #inputs.nixpkgs.url = "github:NixOS/nixpkgs";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let pkgs = nixpkgs.legacyPackages.${system}; in
	{
	devShells.default = pkgs.mkShell {
		buildInputs = with pkgs; [
			poetry
			python311
			pipenv
		];
		};
	}
      );
}
