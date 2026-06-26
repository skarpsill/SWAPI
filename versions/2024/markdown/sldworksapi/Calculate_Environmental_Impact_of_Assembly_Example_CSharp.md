---
title: "Calculate Environmental Impact of an Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Calculate_Environmental_Impact_of_Assembly_Example_CSharp.htm"
---

# Calculate Environmental Impact of an Assembly Example (C#)

This example shows how to calculate the environmental impact of an assembly.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Sustainability primary interop assembly as
 //    a reference (in the IDE's Project Explorer, right-click
 //    the project name, select Add Reference, click the Browse tab,
 //    navigate to the install_dir\api\redist folder and
 //    select SolidWorks.Interop.sustainability.dll).
 // 2. Open:
 //    public_documents\samples\tutorial\api\ZZM7005.sldasm
 // 3. Open an Immediate window.
 // 4. Run to the breakpoint and wait for the environmental impact results to
 //    finish updating in the Sustainability Task Pane.
 // 5. Press F5 to finish.
 //
 // Postconditions: Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere,
 // do not save changes when closing it.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.sustainability;
 using System.Runtime.InteropServices;
 namespace SustAssem_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 asmDoc;
         swgsustainabilityApp sustain;
         SustainabilityMaterial materialInfo;
         SustainabilityAssemblyProcess assemblyProcess;
         SustainabilityAssemblyUse assemblyUse;
         SustainabilityTransportation transInfo;
         SustainabilityEndOfLife eolInfo;

         SustainabilityEnvironmentalImpact environmentalImpactInfo;
         object componentList;
         string[] arrayComponent = new string[3];
         object missingComponentList;
         string materialclass;
         string materialname;
         bool assemblyEnergy;
         object assemblyProcessAmt;
         double[] arrayComponent1 = new double[2];
         double BuildToLast;
         bool energylifespan;
         object assemblyUseAmt;
         double[] arrayComponent2 = new double[6];
         double[] CarbonContent;
         int CarbonValues;
         double[] WaterContent;
         int WaterValues;
         double[] AirContent;
         int AirValues;
         double[] EnergyContent;
         int EnergyValues;
         object output;

         public void Main()
         {
             asmDoc = (ModelDoc2)swApp.ActiveDoc;

             sustain = (swgsustainabilityApp)asmDoc.Extension.GetSustainability();

             // Assign material to assembly components
             Debug.Print("Assign material to assembly components:");
             materialInfo = (SustainabilityMaterial)sustain.GetSustainabilityMaterial();

             arrayComponent[0] = "ZZM7005 End Plate (Default)";
             arrayComponent[1] = "ZZM7005 Silencer (04)";
             arrayComponent[2] = "ZZM7005 Silencer (-)";
             componentList = arrayComponent;

             materialInfo.ExcludeComponent(ref componentList);

             Debug.Print("  Number of components missing materials: " + materialInfo.GetMissingMaterialComponentCount());

             materialInfo.IncludeComponent(ref componentList);

             missingComponentList = materialInfo.GetMissingMaterialComponentList();

             materialInfo.SetPropertiesForComponent(ref missingComponentList);

             materialclass = "Steel";
             materialInfo.MaterialClass = materialclass;
             Debug.Print("  Material class: " + materialclass);

             materialname = "AISI 1020";
             materialInfo.MaterialName = materialname;
             Debug.Print("  Material name: " + materialname);

             materialInfo.ViewResults();

             // Assembly Process
             Debug.Print("Assembly Process:");
             assemblyProcess = sustain.GetSustainabilityAssemblyProcess();

             assemblyProcess.EnergyForAssemblyProcess =  true;
             assemblyEnergy = assemblyProcess.EnergyForAssemblyProcess;

             arrayComponent1[0] = 10.0;
             arrayComponent1[1] = 20.0;
             assemblyProcessAmt = arrayComponent1;
             assemblyProcess.AssemblyProcessAmount = assemblyProcessAmt;

             Debug.Print("  Region of assembly as defined in swSustainabilityRegionName_e: " + assemblyProcess.Region);

             BuildToLast = 21.0;
             assemblyProcess.BuiltToLast = BuildToLast;
             Debug.Print("  Built to last: " + assemblyProcess.BuiltToLast);
             Debug.Print("  Units of time as defined in swSustainabilityDurationType_e: " + assemblyProcess.DurationType);

             // Assembly Use
             Debug.Print("Assembly Use:");
             assemblyUse = sustain.GetSustainabilityAssemblyUse();

             assemblyUse.EnergyOverLifeSpan =  true;
             energylifespan = assemblyUse.EnergyOverLifeSpan;

             arrayComponent2[0] = 10.0;
             arrayComponent2[1] = 20.0;
             arrayComponent2[2] = 30.0;
             arrayComponent2[3] = 40.0;
             arrayComponent2[4] = 50.0;
             arrayComponent2[5] = 60.0;
             assemblyUseAmt = arrayComponent2;
             assemblyUse.AssemblyUseAmount = assemblyUseAmt;
             Debug.Print("  Per units of time as defined in swSustainabilityDurationType_e: " + assemblyUse.DurationType);
             Debug.Print("  Assembly use region as defined in swSustainabilityRegionName_e: " + assemblyUse.AssemblyRegion);

             // Transportation
             Debug.Print("Transportation (in km):");
             transInfo = sustain.GetSustainabilityTransportation();

             Debug.Print("  By train: " + transInfo.Train);
             Debug.Print("  By truck: " + transInfo.Truck);
             Debug.Print("  By boat: " + transInfo.Boat);
             Debug.Print("  By plane: " + transInfo.Plane);

             // End of Life
             Debug.Print("Disposal at end of life:");
             eolInfo = sustain.GetSustainabilityEndOfLife();

             Debug.Print("  % recycled: " + eolInfo.Recycled);
             Debug.Print("  % incinerated: " + eolInfo.Incinerated);
             Debug.Print("  % landfill: " + eolInfo.Landfill);

             // Environmental Impact
             Debug.Print("");
             Debug.Print("Calculated Environmental Impact:");

             environmentalImpactInfo = sustain.GetSustainabilityEnvironmentalImpact();

             Debug.Print(" Time over which to evaluate environmental impact: " + environmentalImpactInfo.DurationOfUse);
             Debug.Print(" Units of time over which to evaluate as defined in swSustainabilityDurationType_e: " + environmentalImpactInfo.DurationType);

             environmentalImpactInfo.UpdateResults();

             System.Diagnostics.Debugger.Break();

             CarbonValues = environmentalImpactInfo.GetCurrentCarbonFootPrint(out output);
             CarbonContent = (Double[])output;
             Debug.Print(" Carbon footprint");
             Debug.Print("  Material: " + CarbonContent[0]);
             Debug.Print("  Use: " + CarbonContent[1]);
             Debug.Print("  Transportation: " + CarbonContent[2]);
             Debug.Print("  Manufacturing: " + CarbonContent[3]);
             Debug.Print("  End of Life: " + CarbonContent[4]);

             WaterValues = environmentalImpactInfo.GetWaterEutrophication(out output);
             WaterContent = (Double[])output;
             Debug.Print(" Water eutrophication");
             Debug.Print("  Material: " + WaterContent[0]);
             Debug.Print("  Use: " + WaterContent[1]);
             Debug.Print("  Transportation: " + WaterContent[2]);
             Debug.Print("  Manufacturing: " + WaterContent[3]);
             Debug.Print("  End of Life: " + WaterContent[4]);

             AirValues = environmentalImpactInfo.GetAirAcidification(out output);
             AirContent = (Double[])output;
             Debug.Print(" Air acidification");
             Debug.Print("  Material: " + AirContent[0]);
             Debug.Print("  Use: " + AirContent[1]);
             Debug.Print("  Transportation: " + AirContent[2]);
             Debug.Print("  Manufacturing: " + AirContent[3]);
             Debug.Print("  End of Life: " + AirContent[4]);

             EnergyValues = environmentalImpactInfo.GetEnergyConsumption(out output);
             EnergyContent = (Double[])output;
             Debug.Print(" Energy consumption");
             Debug.Print("  Material: " + EnergyContent[0]);
             Debug.Print("  Use: " + EnergyContent[1]);
             Debug.Print("  Transportation: " + EnergyContent[2]);
             Debug.Print("  Manufacturing: " + EnergyContent[3]);
             Debug.Print("  End of Life: " + EnergyContent[4]);

         }

         public SldWorks swApp;

     }
 }
```
