---
title: "Get and Set Material Visual Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Material_Visual_Properties_Example_CSharp.htm"
---

# Get and Set Material Visual Properties Example (C#)

This method shows how to get and set the material properties of a part.

```vb
 //-----------------------------------------------------
 // Preconditions:
 // 1. Open a part.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets and sets the part's material visual properties.
 // 2. Inspect the Immediate window and graphics area.
 //------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace ApplyAppearance_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 myModel = default(ModelDoc2);
             PartDoc myPart = default(PartDoc);
             MaterialVisualPropertiesData myMatVisProps = default(MaterialVisualPropertiesData);
             string configName = null;
             string databaseName = null;
             string newPropName = null;
             bool orgBlend = false;
             bool orgApply = false;
             double orgAngle = 0;
             double orgScale = 0;
             long longstatus = 0;

             myModel = (ModelDoc2)swApp.ActiveDoc;
             myPart = (PartDoc)myModel;
             myMatVisProps = myPart.GetMaterialVisualProperties();

             Debug.Print("===== Material Visual Properties Example =====");

             if ((myMatVisProps != null))
             {
                 dump_material_visual_properties(myMatVisProps, myPart);

                 // Set the material to something else, so that the display changes
                 configName =  "default";
                 databaseName = "SOLIDWORKS Materials";
                 newPropName = "Beech";
                 myPart.SetMaterialPropertyName2(configName, databaseName, newPropName);
                 dump_material_visual_properties(myMatVisProps, myPart);
             }

             // Set the material visual properties to be just color, no advanced graphics
             myMatVisProps = myPart.GetMaterialVisualProperties();

             if ((myMatVisProps != null))
             {
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);

                 // Set the material visual properties to be RealView
                 myMatVisProps.RealView = true;
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);

                 // Set the material visual properties to be SOLIDWORKS standard textures
                 myMatVisProps.RealView = false;
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);
             }

             myMatVisProps = myPart.GetMaterialVisualProperties();

             if ((myMatVisProps != null))
             {
                 orgAngle = myMatVisProps.Angle;
                 myMatVisProps.Angle = orgAngle + 1.0;
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);
                 orgScale = myMatVisProps.Scale2;
                 myMatVisProps.Scale2 = orgScale * 1.25;
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);

                 // Toggle the standard texture to blend with the part color
                 if (myMatVisProps.BlendColor == false)
                 {
                     orgBlend = false;
                 }
                 else
                 {
                     orgBlend = true;
                 }

                 myMatVisProps.BlendColor = !orgBlend;
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);
                 myMatVisProps.BlendColor = orgBlend;
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);

                 // Toggle the apply material color to part flag
                 if (myMatVisProps.ApplyMaterialColorToPart ==  false)
                 {
                     orgApply = false;
                 }
                 else
                 {
                     orgApply = true;
                 }

                 myMatVisProps.ApplyMaterialColorToPart = !orgApply;
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);
                 myMatVisProps.ApplyMaterialColorToPart = orgApply;
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);

                 // Toggle the apply material hatch to drawing section view flag
                 if (myMatVisProps.ApplyMaterialHatchToSection ==  false)
                 {
                     orgApply = false;
                 }
                 else
                 {
                     orgApply = true;
                 }

                 myMatVisProps.ApplyMaterialHatchToSection = !orgApply;
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);
                 myMatVisProps.ApplyMaterialHatchToSection = orgApply;
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);

                 // Toggle the apply appearance flag
                 if (myMatVisProps.ApplyAppearance ==  false)
                 {
                     orgApply = false;
                 }
                 else
                 {
                     orgApply = true;
                 }

                 myMatVisProps.ApplyAppearance = !orgApply;
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);
                 myMatVisProps.ApplyAppearance = orgApply;
                 longstatus = myPart.SetMaterialVisualProperties(myMatVisProps, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                 dump_material_visual_properties(myMatVisProps, myPart);
             }

         }

         private void dump_material_visual_properties(MaterialVisualPropertiesData myMatVisProps, PartDoc myPart)
         {
             string configName = null;
             string databaseName = null;
             string propName = null;
             bool bRealView = false;
             double dScale = 0;
             double dAngle = 0;
             bool bBlendColor = false;
             bool bApplyColor = false;
             bool bApplyHatch = false;
             bool bApplyAppearance = false;
             configName = "default";
             databaseName = null;
             propName = myPart.GetMaterialPropertyName2(configName, out databaseName);
             Debug.Print("");
             Debug.Print("Config: \"" + configName +  "\", Database: \"" + databaseName + "\", Material: \"" + propName + "\"");

             if ((myMatVisProps != null))
             {
                 bRealView = myMatVisProps.RealView;
                 dScale = myMatVisProps.Scale2;
                 dAngle = myMatVisProps.Angle;
                 bBlendColor = myMatVisProps.BlendColor;
                 bApplyColor = myMatVisProps.ApplyMaterialColorToPart;
                 bApplyHatch = myMatVisProps.ApplyMaterialHatchToSection;
                 bApplyAppearance = myMatVisProps.ApplyAppearance;

                 if (bRealView == false)
                 {
                     Debug.Print("Advanced graphics - SOLIDWORKS standard textures.");
                 }
                 else
                 {
                     Debug.Print("Advanced graphics - RealView textures.");
                 }
                 Debug.Print("   SOLIDWORKS standard texture scale = " + dScale + ", Angle = " + dAngle);
                 if (bBlendColor == false)
                 {
                     Debug.Print("   Do not blend part color with SOLIDWORKS standard texture.");
                 }
                 else
                 {
                     Debug.Print("   Blend part color with SOLIDWORKS standard texture.");
                 }

                 if (bApplyColor == false)
                 {
                     Debug.Print("Do not apply material color to part.");
                 }
                 else
                 {
                     Debug.Print("Apply material color to part.");
                 }

                 if (bApplyHatch == false)
                 {
                     Debug.Print("Do not apply material hatch to drawing section.");
                 }
                 else
                 {
                     Debug.Print("Apply material hatch to drawing section.");

                 }
                 if (bApplyAppearance == false)
                 {
                     Debug.Print("Do not apply appearance.");
                 }
                 else
                 {
                     Debug.Print("Apply appearance.");
                 }

             }

         }

         public SldWorks swApp;

     }
 }
```
