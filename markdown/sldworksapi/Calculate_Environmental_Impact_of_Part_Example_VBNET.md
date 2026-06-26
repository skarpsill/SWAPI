---
title: "Calculate Environmental Impact of Part (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Calculate_Environmental_Impact_of_Part_Example_VBNET.htm"
---

# Calculate Environmental Impact of Part (VB.NET)

This example shows how to calculate the environmental impact of a part.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Sustainability primary interop assembly as
 '    a reference (in the IDE's Project Explorer, right-click
 '    the project name, select Add Reference, click the Browse tab,
 '    navigate to the install_dir\api\redist folder and
 '    select SolidWorks.Interop.sustainability.dll).
 ' 2. Open:
 '    public_documents\samples\tutorial\api\ZZM7005 End Plate.sldprt
 ' 3. Open an Immediate window.
 ' 4. Run to the breakpoint and wait for the environmental impact results to
 '    finish updating in the Sustainability Task Pane.
 ' 5. Press F5 to finish.
 '
 ' Postconditions: Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere,
 ' do not save changes when closing it.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.sustainability
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModelDoc As ModelDoc2

     Sub main()

         Dim PDoc As ModelDoc2
         PDoc = swApp.ActiveDoc

         Dim sustain As swgsustainabilityApp
         sustain = PDoc.Extension.GetSustainability

         ' Material
         Debug.Print("Material:")
         Dim materialInfo As SustainabilityMaterial
         materialInfo = sustain.GetSustainabilityMaterial

         Dim MaterialClass As String
         MaterialClass =  "Plastics"
         materialInfo.MaterialClass = MaterialClass
         Debug.Print(" Material class: " & MaterialClass)

         Dim MaterialName As String
         MaterialName =  "ABS"
         materialInfo.MaterialName = MaterialName
         Debug.Print(" Material name: " & MaterialName)

         Debug.Print(" % recycled: " & materialInfo.RecycledContent)
         Debug.Print(" Weight: " & materialInfo.Weight)

         ' Manufacturing
         Debug.Print("Manufacturing:")
         Dim manufacturingInfo As SustainabilityManufacturing
         manufacturingInfo = sustain.GetSustainabilityManufacturing

         Debug.Print(" Region: " & manufacturingInfo.ManufacturingRegion)
         Debug.Print(" Built to last: " & manufacturingInfo.BuiltToLast)
         Debug.Print(" Process: " & manufacturingInfo.ManufacturingProcess)
         Debug.Print(" Primary electricity: " & manufacturingInfo.PrimaryElectricity)
         Debug.Print(" Primary natural gas: " & manufacturingInfo.PrimaryNaturalGas)
         Debug.Print(" Primary scrap rate: " & manufacturingInfo.PrimaryScrapRate)
         Debug.Print(" Paint: " & manufacturingInfo.Paint)
         Debug.Print(" Surface area: " & manufacturingInfo.SurfaceArea)

         ' Transportation
         Debug.Print("Transportation:")
         Dim transInfo As SustainabilityTransportation
         transInfo = sustain.GetSustainabilityTransportation

         Debug.Print(" By train: " & transInfo.Train)
         Debug.Print(" By truck: " & transInfo.Truck)
         Debug.Print(" By boat: " & transInfo.Boat)
         Debug.Print(" By plane: " & transInfo.Plane)

         ' Disposal at end of life
         Debug.Print("Disposal at end of life:")
         Dim eofInfo As SustainabilityEndOfLife
         eofInfo = sustain.GetSustainabilityEndOfLife

         Debug.Print(" % recycled: " & eofInfo.Recycled)
         Debug.Print(" % incinerated: " & eofInfo.Incinerated)
         Debug.Print(" % landfill: " & eofInfo.Landfill)

         ' Use
         Debug.Print("Use:")
         Dim partInfo As SustainabilityPartUse
         partInfo = sustain.GetSustainabilityPartUse

         Debug.Print(" Region of use: " & partInfo.Region)

         Stop

         ' Environmental impact
         Debug.Print("Environmental impact:")
         Dim environmentalImpactInfo As SustainabilityEnvironmentalImpact
         environmentalImpactInfo = sustain.GetSustainabilityEnvironmentalImpact

         Dim CarbonValues As Integer
         Dim CarbonContent As Object = Nothing
         CarbonValues = environmentalImpactInfo.GetCurrentCarbonFootPrint(CarbonContent)
         Debug.Print(" Carbon footprint")
         Debug.Print("  Material: " & CarbonContent(0))
         Debug.Print("  Use: " & CarbonContent(1))
         Debug.Print("  Transportation: " & CarbonContent(2))
         Debug.Print("  Manufacturing: " & CarbonContent(3))
         Debug.Print("  End of Life: " & CarbonContent(4))

         Dim WaterValues As Integer
         Dim WaterContent As Object = Nothing
         WaterValues = environmentalImpactInfo.GetWaterEutrophication(WaterContent)
         Debug.Print(" Water eutrophication")
         Debug.Print("  Material: " & WaterContent(0))
         Debug.Print("  Use: " & WaterContent(1))
         Debug.Print("  Transportation: " & WaterContent(2))
         Debug.Print("  Manufacturing: " & WaterContent(3))
         Debug.Print("  End of Life: " & WaterContent(4))

         Dim AirValues As Integer
         Dim AirContent As Object = Nothing
         AirValues = environmentalImpactInfo.GetAirAcidification(AirContent)
         Debug.Print(" Air acidification")
         Debug.Print("  Material: " & AirContent(0))
         Debug.Print("  Use: " & AirContent(1))
         Debug.Print("  Transportation: " & AirContent(2))
         Debug.Print("  Manufacturing: " & AirContent(3))
         Debug.Print("  End of Life: " & AirContent(4))

         Dim EnergyValues As Integer
         Dim EnergyContent As Object = Nothing
         EnergyValues = environmentalImpactInfo.GetEnergyConsumption(EnergyContent)
         Debug.Print(" Energy consumption")
         Debug.Print("  Material: " & EnergyContent(0))
         Debug.Print("  Use: " & EnergyContent(1))
         Debug.Print("  Transportation: " & EnergyContent(2))
         Debug.Print("  Manufacturing: " & EnergyContent(3))
         Debug.Print("  End of Life: " & EnergyContent(4))

     End Sub

     Public swApp As SldWorks

 End  Class
```
