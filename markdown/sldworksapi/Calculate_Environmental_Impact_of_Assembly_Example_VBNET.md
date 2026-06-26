---
title: "Calculate Environmental Impact of an Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Calculate_Environmental_Impact_of_Assembly_Example_VBNET.htm"
---

# Calculate Environmental Impact of an Assembly Example (VB.NET)

This example shows how to calculate the environmental impact of an assembly.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Sustainability primary interop assembly as
 '    a reference (in the IDE's Project Explorer, right-click
 '    the project name, select Add Reference, click the Browse tab,
 '    navigate to the install_dir\api\redist folder and
 '    select SolidWorks.Interop.sustainability.dll).
 ' 2. Open:
 '    public_documents\samples\tutorial\api\ZZM7005.sldasm
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

     Dim asmDoc As ModelDoc2
     Dim sustain As swgsustainabilityApp
     Dim materialInfo As SustainabilityMaterial
     Dim assemblyProcess As SustainabilityAssemblyProcess
     Dim assemblyUse As SustainabilityAssemblyUse
     Dim transInfo As SustainabilityTransportation
     Dim eolInfo As SustainabilityEndOfLife
     Dim environmentalImpactInfo As SustainabilityEnvironmentalImpact

     Dim componentList As Object
     Dim arrayComponent(2) As String
     Dim missingComponentList As Object
     Dim materialclass As String
     Dim materialname As String
     Dim assemblyEnergy As Boolean
     Dim assemblyProcessAmt As Object
     Dim arrayComponent1(1) As Double
     Dim BuildToLast As Double
     Dim energylifespan As Boolean
     Dim assemblyUseAmt As Object
     Dim arrayComponent2(5) As Double
     Dim CarbonContent As Object
     Dim CarbonValues As Integer
     Dim WaterContent As Object
     Dim WaterValues As Integer
     Dim AirContent As Object
     Dim AirValues As Integer
     Dim EnergyContent As Object
     Dim EnergyValues As Integer

     Sub main()

         asmDoc = swApp.ActiveDoc

         sustain = asmDoc.Extension.GetSustainability

         ' Assign material to assembly components
         Debug.Print("Assign material to assembly components:")
         materialInfo = sustain.GetSustainabilityMaterial

         arrayComponent(0) = "ZZM7005 End Plate (Default)"
         arrayComponent(1) =  "ZZM7005 Silencer (04)"
         arrayComponent(2) =  "ZZM7005 Silencer (-)"
         componentList = arrayComponent

         materialInfo.ExcludeComponent(arrayComponent(0).ToString())

         Debug.Print("  Number of components missing materials: " & materialInfo.GetMissingMaterialComponentCount)

         materialInfo.IncludeComponent(arrayComponent(0).ToString())

         missingComponentList = materialInfo.GetMissingMaterialComponentList

         materialInfo.SetPropertiesForComponent(missingComponentList)

         materialclass = "Steel"
         materialInfo.materialclass = materialclass
         Debug.Print("  Material class: " & materialclass)

         materialname = "AISI 1020"
         materialInfo.materialname = materialname
         Debug.Print("  Material name: " & materialname)

         materialInfo.ViewResults()

         ' Assembly Process
         Debug.Print("Assembly Process:")
         assemblyProcess = sustain.GetSustainabilityAssemblyProcess

         assemblyProcess.EnergyForAssemblyProcess =  True
         assemblyEnergy = assemblyProcess.EnergyForAssemblyProcess

         arrayComponent1(0) = 10.0#
         arrayComponent1(1) = 20.0#
         assemblyProcessAmt = arrayComponent1
         assemblyProcess.AssemblyProcessAmount = assemblyProcessAmt

         Debug.Print("  Region of assembly as defined in swSustainabilityRegionName_e: " & assemblyProcess.region)

         BuildToLast = 21.0#
         assemblyProcess.BuiltToLast = BuildToLast
         Debug.Print("  Built to last: " & assemblyProcess.BuiltToLast)
         Debug.Print("  Units of time as defined in swSustainabilityDurationType_e: " & assemblyProcess.durationType)

         ' Assembly Use
         Debug.Print("Assembly Use:")
         assemblyUse = sustain.GetSustainabilityAssemblyUse

         assemblyUse.energyOverlifeSpan =  True
         energylifespan = assemblyUse.energyOverlifeSpan

         arrayComponent2(0) = 10.0#
         arrayComponent2(1) = 20.0#
         arrayComponent2(2) = 30.0#
         arrayComponent2(3) = 40.0#
         arrayComponent2(4) = 50.0#
         arrayComponent2(5) = 60.0#
         assemblyUseAmt = arrayComponent2
         assemblyUse.AssemblyUseAmount = assemblyUseAmt
         Debug.Print("  Per units of time as defined in swSustainabilityDurationType_e: " & assemblyUse.durationType)
         Debug.Print("  Assembly use region as defined in swSustainabilityRegionName_e: " & assemblyUse.AssemblyRegion)

         ' Transportation
         Debug.Print("Transportation (in km):")
         transInfo = sustain.GetSustainabilityTransportation

         Debug.Print("  By train: " & transInfo.Train)
         Debug.Print("  By truck: " & transInfo.Truck)
         Debug.Print("  By boat: " & transInfo.Boat)
         Debug.Print("  By plane: " & transInfo.Plane)

         ' End of Life
         Debug.Print("Disposal at end of life:")
         eolInfo = sustain.GetSustainabilityEndOfLife

         Debug.Print("  % recycled: " & eolInfo.recycled)
         Debug.Print("  % incinerated: " & eolInfo.incinerated)
         Debug.Print("  % landfill: " & eolInfo.landfill)

         ' Environmental Impact
         Debug.Print("")
         Debug.Print("Calculated Environmental Impact:")

         environmentalImpactInfo = sustain.GetSustainabilityEnvironmentalImpact

         Debug.Print(" Time over which to evaluate environmental impact: " & environmentalImpactInfo.durationofuse)
         Debug.Print(" Units of time over which to evaluate as defined in swSustainabilityDurationType_e: " & environmentalImpactInfo.durationType)

         environmentalImpactInfo.UpdateResults()

         Stop

         CarbonValues = environmentalImpactInfo.GetCurrentCarbonFootPrint(CarbonContent)
         Debug.Print(" Carbon footprint")
         Debug.Print("  Material: " & CarbonContent(0))
         Debug.Print("  Use: " & CarbonContent(1))
         Debug.Print("  Transportation: " & CarbonContent(2))
         Debug.Print("  Manufacturing: " & CarbonContent(3))
         Debug.Print("  End of Life: " & CarbonContent(4))

         WaterValues = environmentalImpactInfo.GetWaterEutrophication(WaterContent)
         Debug.Print(" Water eutrophication")
         Debug.Print("  Material: " & WaterContent(0))
         Debug.Print("  Use: " & WaterContent(1))
         Debug.Print("  Transportation: " & WaterContent(2))
         Debug.Print("  Manufacturing: " & WaterContent(3))
         Debug.Print("  End of Life: " & WaterContent(4))

         AirValues = environmentalImpactInfo.GetAirAcidification(AirContent)
         Debug.Print(" Air acidification")
         Debug.Print("  Material: " & AirContent(0))
         Debug.Print("  Use: " & AirContent(1))
         Debug.Print("  Transportation: " & AirContent(2))
         Debug.Print("  Manufacturing: " & AirContent(3))
         Debug.Print("  End of Life: " & AirContent(4))

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
