// Artenuvielle: This file is adopted from https://github.com/code4game/libprotobuf

using UnrealBuildTool;

public class enet : ModuleRules
{
    public enet(ReadOnlyTargetRules Target) : base(Target)
    {
        Type = ModuleType.External;

        bool is_supported = false;
        if (Target.Platform == UnrealTargetPlatform.Win64)
        {
            is_supported = true;

            string enet_lib_directory_full_path = System.IO.Path.Combine(ModuleDirectoryFullPath, "lib", "win64");
            PublicLibraryPaths.Add(enet_lib_directory_full_path);
            PublicAdditionalLibraries.Add("enet.lib");
        }
        else if(Target.Platform == UnrealTargetPlatform.Linux)
        {
            is_supported = false;
        }
        
        if (is_supported)
        {
            string enet_code_directory_full_path = System.IO.Path.Combine(ModuleDirectoryFullPath, "include");

            PublicSystemIncludePaths.Add(enet_code_directory_full_path);
        }
    }

    string ModuleDirectoryFullPath
    {
        get { return System.IO.Path.GetFullPath(ModuleDirectory); }
    }
}

