enet for [Unreal Engine 4][]
=====

Links the enet library as the third party in [Unreal Engine 4][].

Prerequisites
-------------

* Python v3 (for install and build scripts)
* [CMake][] and either Visual Studio 2015 or Visual Studio 2017

Usage
-----

1. Clone or add this repository as submodule to your project directory.
2. Go into the just created directory and run `./install.py`. This will build enet and copy the compiled version into the ThirdParty directory of your project (`<your project>/Source/ThirdParty/enet`).
3. Add theenet as a module into `<your project>.Build.cs`
  * `PrivateDependencyModuleNames.AddRange(new string[] { "enet" });`
4. Add the include directory to the include path of your compiler (e.g.: `$(SolutionDir)Source\ThirdParty\enet\inlude;$(IncludePath)`). 

TODO
----
* Add linux support
