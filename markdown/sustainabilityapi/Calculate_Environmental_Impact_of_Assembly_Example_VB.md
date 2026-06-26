---
title: "Calculate Environmental Impact of an Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sustainabilityapi/Calculate_Environmental_Impact_of_Assembly_Example_VB.htm"
---

# Calculate Environmental Impact of an Assembly Example (VBA)

This example shows how to calculate the environmental impact of an assembly.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Select Tools > References > sustainability 20xx Type Library or
 '    click Tools > References > Browse... and select  install_dir\sustainability.tlb.
 ' 2. Open an assembly.
 ' 3. Open an Immediate window.
 ' 4. Run to the breakpoint and wait for the environmental impact results to
 '    finish updating in the Sustainability Task Pane.
 ' 5. Press F5 to finish.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate window.
 ' 2. C:\EnvImpactReport.docx is created and opened.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim asmDoc As SldWorks.ModelDoc2
 Dim sustain As sustainabilityLib.sustainabilityApp
 Dim materialInfo As sustainabilityLib.SustainabilityMaterial
 Dim assemblyProcess As sustainabilityLib.SustainabilityAssemblyProcess
 Dim assemblyUse As sustainabilityLib.SustainabilityAssemblyUse
 Dim transInfo As sustainabilityLib.SustainabilityTransportation
 Dim eolInfo As sustainabilityLib.SustainabilityEndOfLife
 Dim environmentalImpactInfo As sustainabilityLib.SustainabilityEnvironmentalImpact
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
 Dim CarbonValues As Variant
 Dim WaterValues As Variant
 Dim AirValues As Variant
 Dim EnergyValues As Variant

Option Explicit
 Sub main()
    Set swApp = Application.SldWorks

    Set asmDoc = swApp.ActiveDoc

    Set sustain = asmDoc.Extension.GetSustainability

    ' Assign material to assembly components
     Debug.Print "Assign material to assembly components:"
     Set materialInfo = sustain.GetSustainabilityMaterial

    Debug.Print "  Number of components missing materials: " & materialInfo.GetMissingMaterialComponentCount

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

    CarbonValues = environmentalImpactInfo.GetCurrentCarbonFootPrint2
     Debug.Print " Carbon footprint"
     Debug.Print "  Material: " & CarbonValues(0)
     Debug.Print "  Use: " & CarbonValues(1)
     Debug.Print "  Transportation: " & CarbonValues(2)
     Debug.Print "  Manufacturing: " & CarbonValues(3)
     Debug.Print "  End of Life: " & CarbonValues(4)

    WaterValues = environmentalImpactInfo.GetWaterEutrophication2
     Debug.Print " Water eutrophication"
     Debug.Print "  Material: " & WaterValues(0)
     Debug.Print "  Use: " & WaterValues(1)
     Debug.Print "  Transportation: " & WaterValues(2)
     Debug.Print "  Manufacturing: " & WaterValues(3)
     Debug.Print "  End of Life: " & WaterValues(4)

    AirValues = environmentalImpactInfo.GetAirAcidification2
     Debug.Print " Air acidification"
     Debug.Print "  Material: " & AirValues(0)
     Debug.Print "  Use: " & AirValues(1)
     Debug.Print "  Transportation: " & AirValues(2)
     Debug.Print "  Manufacturing: " & AirValues(3)
     Debug.Print "  End of Life: " & AirValues(4)

    EnergyValues = environmentalImpactInfo.GetEnergyConsumption2
     Debug.Print " Energy consumption"
     Debug.Print "  Material: " & EnergyValues(0)
     Debug.Print "  Use: " & EnergyValues(1)
     Debug.Print "  Transportation: " & EnergyValues(2)
     Debug.Print "  Manufacturing: " & EnergyValues(3)
     Debug.Print "  End of Life: " & EnergyValues(4)

    Dim FileType As Long
     Dim FileName As String
     Dim SaveTo As String

     FileType = swSustainabilitySaveAsFileType_e.swSustainabilityDocxReport
     FileName = "EnvImpactReport"
     SaveTo = "C:\"
    environmentalImpactInfo.SaveAsReport FileType, FileName, SaveTo

End Sub
```
