---
title: "Calculate Environmental Impact of an Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Calculate_Environmental_Impact_of_Assembly_Example_VB.htm"
---

# Calculate Environmental Impact of an Assembly Example (VBA)

This example shows how to calculate the environmental impact of an assembly.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open:
 '    public_documents\samples\tutorial\api\ZZM7005.sldasm
 ' 2. Open an Immediate window.
 ' 3. Run to the breakpoint and wait for the environmental impact results to
 '    finish updating in the Sustainability Task Pane.
 ' 4. Press F5 to finish.
 '
 ' Postconditions: Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere,
 ' do not save changes when closing it.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim asmDoc As SldWorks.ModelDoc2
 Dim sustain As sustainabilityLib.swgsustainabilityApp
 Dim materialInfo As sustainabilityLib.SustainabilityMaterial
 Dim assemblyProcess As sustainabilityLib.SustainabilityAssemblyProcess
 Dim assemblyUse As sustainabilityLib.SustainabilityAssemblyUse
 Dim transInfo As sustainabilityLib.SustainabilityTransportation
 Dim eolInfo As sustainabilityLib.SustainabilityEndOfLife
 Dim environmentalImpactInfo As sustainabilityLib.SustainabilityEnvironmentalImpact
Dim componentList As Variant
 Dim arrayComponent(2) As String
 Dim missingComponentList As Variant
 Dim materialclass As String
 Dim materialname As String
 Dim assemblyEnergy As Boolean
 Dim assemblyProcessAmt As Variant
 Dim arrayComponent1(1) As Double
 Dim BuildToLast As Double
 Dim energylifespan As Boolean
 Dim assemblyUseAmt As Variant
 Dim arrayComponent2(5) As Double
 Dim CarbonContent As Variant
 Dim CarbonValues As Long
 Dim WaterContent As Variant
 Dim WaterValues As Long
 Dim AirContent As Variant
 Dim AirValues As Long
 Dim EnergyContent As Variant
 Dim EnergyValues As Long

Option Explicit
 Sub main()
    Set swApp = Application.SldWorks

    Set asmDoc = swApp.ActiveDoc

    Set sustain = asmDoc.Extension.GetSustainability

    ' Assign material to assembly components
     Debug.Print "Assign material to assembly components:"
     Set materialInfo = sustain.GetSustainabilityMaterial

    arrayComponent(0) = "ZZM7005 End Plate (Default)"
     arrayComponent(1) = "ZZM7005 Silencer (04)"
     arrayComponent(2) = "ZZM7005 Silencer (-)"
     componentList = arrayComponent

    materialInfo.ExcludeComponent (arrayComponent(0))

    Debug.Print "  Number of components missing materials: " & materialInfo.GetMissingMaterialComponentCount

    materialInfo.IncludeComponent (arrayComponent(0))

    missingComponentList = materialInfo.GetMissingMaterialComponentList

    materialInfo.SetPropertiesForComponent (missingComponentList)

    materialclass = "Steel"
     materialInfo.materialclass = materialclass
     Debug.Print "  Material class: " & materialclass

    materialname = "AISI 1020"
     materialInfo.materialname = materialname
     Debug.Print "  Material name: " & materialname

    materialInfo.ViewResults

    ' Assembly Process
     Debug.Print "Assembly Process:"
     Set assemblyProcess = sustain.GetSustainabilityAssemblyProcess

    assemblyProcess.EnergyForAssemblyProcess = True
     assemblyEnergy = assemblyProcess.EnergyForAssemblyProcess

    arrayComponent1(0) = 10#
     arrayComponent1(1) = 20#
     assemblyProcessAmt = arrayComponent1
     assemblyProcess.AssemblyProcessAmount = assemblyProcessAmt

    Debug.Print "  Region of assembly as defined in swSustainabilityRegionName_e: " & assemblyProcess.region

    BuildToLast = 21#
     assemblyProcess.BuiltToLast = BuildToLast
     Debug.Print "  Built to last: " & assemblyProcess.BuiltToLast
     Debug.Print "  Units of time as defined in swSustainabilityDurationType_e: " & assemblyProcess.durationType

    ' Assembly Use
     Debug.Print "Assembly Use:"
     Set assemblyUse = sustain.GetSustainabilityAssemblyUse

    assemblyUse.energyOverlifeSpan = True
     energylifespan = assemblyUse.energyOverlifeSpan

    arrayComponent2(0) = 10#
     arrayComponent2(1) = 20#
     arrayComponent2(2) = 30#
     arrayComponent2(3) = 40#
     arrayComponent2(4) = 50#
     arrayComponent2(5) = 60#
     assemblyUseAmt = arrayComponent2
     assemblyUse.AssemblyUseAmount = assemblyUseAmt
     Debug.Print "  Per units of time as defined in swSustainabilityDurationType_e: " & assemblyUse.durationType
     Debug.Print "  Assembly use region as defined in swSustainabilityRegionName_e: " & assemblyUse.AssemblyRegion

    ' Transportation
     Debug.Print "Transportation (in km):"
     Set transInfo = sustain.GetSustainabilityTransportation

    Debug.Print "  By train: " & transInfo.Train
     Debug.Print "  By truck: " & transInfo.Truck
     Debug.Print "  By boat: " & transInfo.Boat
     Debug.Print "  By plane: " & transInfo.Plane

    ' End of Life
     Debug.Print "Disposal at end of life:"
     Set eolInfo = sustain.GetSustainabilityEndOfLife

    Debug.Print "  % recycled: " & eolInfo.recycled
     Debug.Print "  % incinerated: " & eolInfo.incinerated
     Debug.Print "  % landfill: " & eolInfo.landfill

    ' Environmental Impact
     Debug.Print ""
     Debug.Print "Calculated Environmental Impact:"

    Set environmentalImpactInfo = sustain.GetSustainabilityEnvironmentalImpact

    Debug.Print " Time over which to evaluate environmental impact: " & environmentalImpactInfo.durationofuse
     Debug.Print " Units of time over which to evaluate as defined in swSustainabilityDurationType_e: " & environmentalImpactInfo.durationType

    environmentalImpactInfo.UpdateResults

    Stop

    CarbonValues = environmentalImpactInfo.GetCurrentCarbonFootPrint(CarbonContent)
     Debug.Print " Carbon footprint"
     Debug.Print "  Material: " & CarbonContent(0)
     Debug.Print "  Use: " & CarbonContent(1)
     Debug.Print "  Transportation: " & CarbonContent(2)
     Debug.Print "  Manufacturing: " & CarbonContent(3)
     Debug.Print "  End of Life: " & CarbonContent(4)

    WaterValues = environmentalImpactInfo.GetWaterEutrophication(WaterContent)
     Debug.Print " Water eutrophication"
     Debug.Print "  Material: " & WaterContent(0)
     Debug.Print "  Use: " & WaterContent(1)
     Debug.Print "  Transportation: " & WaterContent(2)
     Debug.Print "  Manufacturing: " & WaterContent(3)
     Debug.Print "  End of Life: " & WaterContent(4)

    AirValues = environmentalImpactInfo.GetAirAcidification(AirContent)
     Debug.Print " Air acidification"
     Debug.Print "  Material: " & AirContent(0)
     Debug.Print "  Use: " & AirContent(1)
     Debug.Print "  Transportation: " & AirContent(2)
     Debug.Print "  Manufacturing: " & AirContent(3)
     Debug.Print "  End of Life: " & AirContent(4)

    EnergyValues = environmentalImpactInfo.GetEnergyConsumption(EnergyContent)
     Debug.Print " Energy consumption"
     Debug.Print "  Material: " & EnergyContent(0)
     Debug.Print "  Use: " & EnergyContent(1)
     Debug.Print "  Transportation: " & EnergyContent(2)
     Debug.Print "  Manufacturing: " & EnergyContent(3)
     Debug.Print "  End of Life: " & EnergyContent(4)

End Sub
```
