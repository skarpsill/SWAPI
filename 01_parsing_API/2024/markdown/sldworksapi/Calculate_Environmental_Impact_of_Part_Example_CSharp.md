---
title: "Calculate Environmental Impact of Part (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Calculate_Environmental_Impact_of_Part_Example_CSharp.htm"
---

# Calculate Environmental Impact of Part (C#)

This example shows how to calculate the environmental impact of a part.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Sustainability primary interop assembly as
 //    a reference (in the IDE's Project Explorer, right-click
 //    the project name, select Add Reference, click the Browse tab,
 //    navigate to the install_dir\api\redist folder and
 //    select SolidWorks.Interop.sustainability.dll).
 // 2. Open:
 //    public_documents\samples\tutorial\api\ZZM7005 End Plate.sldprt
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
 namespace SustPart_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 PDoc = default(ModelDoc2);
             PDoc = (ModelDoc2)swApp.ActiveDoc;

             swgsustainabilityApp sustain = default(swgsustainabilityApp);
             sustain = (swgsustainabilityApp)PDoc.Extension.GetSustainability();

             // Material
             Debug.Print("Material:");
             SustainabilityMaterial materialInfo = default(SustainabilityMaterial);
             materialInfo = sustain.GetSustainabilityMaterial();

             string MaterialClass = null;
             MaterialClass = "Plastics";
             materialInfo.MaterialClass = MaterialClass;
             Debug.Print(" Material class: " + MaterialClass);

             string MaterialName = null;
             MaterialName = "ABS";
             materialInfo.MaterialName = MaterialName;
             Debug.Print(" Material name: " + MaterialName);

             Debug.Print(" % recycled: " + materialInfo.RecycledContent);
             Debug.Print(" Weight: " + materialInfo.Weight);

             // Manufacturing
             Debug.Print("Manufacturing:");
             SustainabilityManufacturing manufacturingInfo = default(SustainabilityManufacturing);
             manufacturingInfo = sustain.GetSustainabilityManufacturing();

             Debug.Print(" Region: " + manufacturingInfo.ManufacturingRegion);
             Debug.Print(" Built to last: " + manufacturingInfo.BuiltToLast);
             Debug.Print(" Process: " + manufacturingInfo.ManufacturingProcess);
             Debug.Print(" Primary electricity: " + manufacturingInfo.PrimaryElectricity);
             Debug.Print(" Primary natural gas: " + manufacturingInfo.PrimaryNaturalGas);
             Debug.Print(" Primary scrap rate: " + manufacturingInfo.PrimaryScrapRate);
             Debug.Print(" Paint: " + manufacturingInfo.Paint);
             Debug.Print(" Surface area: " + manufacturingInfo.SurfaceArea);

             // Transportation
             Debug.Print("Transportation:");
             SustainabilityTransportation transInfo = default(SustainabilityTransportation);
             transInfo = sustain.GetSustainabilityTransportation();

             Debug.Print(" By train: " + transInfo.Train);
             Debug.Print(" By truck: " + transInfo.Truck);
             Debug.Print(" By boat: " + transInfo.Boat);
             Debug.Print(" By plane: " + transInfo.Plane);

             // Disposal at end of life
             Debug.Print("Disposal at end of life:");
             SustainabilityEndOfLife eofInfo = default(SustainabilityEndOfLife);
             eofInfo = sustain.GetSustainabilityEndOfLife();

             Debug.Print(" % recycled: " + eofInfo.Recycled);
             Debug.Print(" % incinerated: " + eofInfo.Incinerated);
             Debug.Print(" % landfill: " + eofInfo.Landfill);

             // Use
             Debug.Print("Use:");
             SustainabilityPartUse partInfo = default(SustainabilityPartUse);
             partInfo = sustain.GetSustainabilityPartUse();

             Debug.Print(" Region of use: " + partInfo.Region);

             System.Diagnostics.Debugger.Break();

             // Environmental impact
             Debug.Print("Environmental impact:");
             SustainabilityEnvironmentalImpact environmentalImpactInfo = default(SustainabilityEnvironmentalImpact);
             environmentalImpactInfo = sustain.GetSustainabilityEnvironmentalImpact();

             int CarbonValues = 0;
             object output = null;
             Double[] CarbonContent;
             CarbonValues = environmentalImpactInfo.GetCurrentCarbonFootPrint(out output);
             CarbonContent = (Double[])output;
             Debug.Print(" Carbon footprint");
             Debug.Print("  Material: " + CarbonContent[0]);
             Debug.Print("  Use: " + CarbonContent[1]);
             Debug.Print("  Transportation: " + CarbonContent[2]);
             Debug.Print("  Manufacturing: " + CarbonContent[3]);
             Debug.Print("  End of Life: " + CarbonContent[4]);

             int WaterValues = 0;
             output = null;
             Double[] WaterContent;
             WaterValues = environmentalImpactInfo.GetWaterEutrophication(out output);
             WaterContent = (Double[])output;
             Debug.Print(" Water eutrophication");
             Debug.Print("  Material: " + WaterContent[0]);
             Debug.Print("  Use: " + WaterContent[1]);
             Debug.Print("  Transportation: " + WaterContent[2]);
             Debug.Print("  Manufacturing: " + WaterContent[3]);
             Debug.Print("  End of Life: " + WaterContent[4]);

             int AirValues = 0;
             output = null;
             Double[] AirContent;
             AirValues = environmentalImpactInfo.GetAirAcidification(out output);
             AirContent = (Double[])output;
             Debug.Print(" Air acidification");
             Debug.Print("  Material: " + AirContent[0]);
             Debug.Print("  Use: " + AirContent[1]);
             Debug.Print("  Transportation: " + AirContent[2]);
             Debug.Print("  Manufacturing: " + AirContent[3]);
             Debug.Print("  End of Life: " + AirContent[4]);

             int EnergyValues = 0;
             output = null;
             Double[] EnergyContent;
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
