---
title: "Calculate Environmental Impact of Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sustainabilityapi/Calculate_Environmental_Impact_of_Part_Example_VB.htm"
---

# Calculate Environmental Impact of Part Example (VBA)

This example shows how to calculate the environmental impact of a part.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part.
 ' 2. Open an Immediate window.
 ' 3. Run to the breakpoint and wait for the environmental impact results to
 '    finish updating in the Sustainability Task Pane.
 ' 4. Press F5 to finish.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate window.
 ' 2. C:\EnvImpactReport.docx is created and opened.
 ' ---------------------------------------------------------------------------

 Dim swApp As SldWorks.SldWorks
 Dim swModelDoc As SldWorks.ModelDoc2
Option Explicit

Sub main()

    Set swApp = Application.SldWorks

    Dim PDoc As SldWorks.ModelDoc2
     Set PDoc = swApp.ActiveDoc

    Dim sustain As sustainabilityLib.sustainabilityApp
     Set sustain = PDoc.Extension.GetSustainability

    ' Material
     Debug.Print "Material:"
     Dim materialInfo As sustainabilityLib.SustainabilityMaterial
     Set materialInfo = sustain.GetSustainabilityMaterial

    Dim MaterialClass As String
     MaterialClass = "Plastics"
     materialInfo.MaterialClass = MaterialClass
     Debug.Print " Material class: " & MaterialClass

    Dim MaterialName As String
     MaterialName = "ABS"
     materialInfo.MaterialName = MaterialName
     Debug.Print " Material name: " & MaterialName

    Debug.Print " % recycled: " & materialInfo.RecycledContent
     Debug.Print " Weight: " & materialInfo.Weight

    ' Manufacturing
     Debug.Print "Manufacturing:"
     Dim manufacturingInfo As sustainabilityLib.SustainabilityManufacturing
     Set manufacturingInfo = sustain.GetSustainabilityManufacturing

    Debug.Print " Region: " & manufacturingInfo.ManufacturingRegion
     Debug.Print " Built to last: " & manufacturingInfo.BuiltToLast
     Debug.Print " Process: " & manufacturingInfo.ManufacturingProcess
     Debug.Print " Primary electricity: " & manufacturingInfo.PrimaryElectricity
     Debug.Print " Primary natural gas: " & manufacturingInfo.PrimaryNaturalGas
     Debug.Print " Primary scrap rate: " & manufacturingInfo.PrimaryScrapRate
     Debug.Print " Paint: " & manufacturingInfo.Paint
     Debug.Print " Surface area: " & manufacturingInfo.SurfaceArea

    ' Transportation
     Debug.Print "Transportation:"
     Dim transInfo As sustainabilityLib.SustainabilityTransportation
     Set transInfo = sustain.GetSustainabilityTransportation

    Debug.Print " By train: " & transInfo.Train
     Debug.Print " By truck: " & transInfo.Truck
     Debug.Print " By boat: " & transInfo.Boat
     Debug.Print " By plane: " & transInfo.Plane

    ' Disposal at end of life
     Debug.Print "Disposal at end of life:"
     Dim eofInfo As sustainabilityLib.SustainabilityEndOfLife
     Set eofInfo = sustain.GetSustainabilityEndOfLife

    Debug.Print " % recycled: " & eofInfo.Recycled
     Debug.Print " % incinerated: " & eofInfo.Incinerated
     Debug.Print " % landfill: " & eofInfo.Landfill

    ' Use
     Debug.Print "Use:"
     Dim partInfo As sustainabilityLib.SustainabilityPartUse
     Set partInfo = sustain.GetSustainabilityPartUse

    Debug.Print " Region of use: " & partInfo.Region

    Stop

    ' Environmental impact
     Debug.Print "Environmental impact:"
     Dim environmentalImpactInfo As sustainabilityLib.SustainabilityEnvironmentalImpact
     Set environmentalImpactInfo = sustain.GetSustainabilityEnvironmentalImpact

    Dim CarbonValues As Variant
     CarbonValues = environmentalImpactInfo.GetCurrentCarbonFootPrint2
     Debug.Print " Carbon footprint"
     Debug.Print "  Material: " & CarbonValues(0)
     Debug.Print "  Use: " & CarbonValues(1)
     Debug.Print "  Transportation: " & CarbonValues(2)
     Debug.Print "  Manufacturing: " & CarbonValues(3)
     Debug.Print "  End of Life: " & CarbonValues(4)

    Dim WaterValues As Variant
     WaterValues = environmentalImpactInfo.GetWaterEutrophication2
     Debug.Print " Water eutrophication"
     Debug.Print "  Material: " & WaterValues(0)
     Debug.Print "  Use: " & WaterValues(1)
     Debug.Print "  Transportation: " & WaterValues(2)
     Debug.Print "  Manufacturing: " & WaterValues(3)
     Debug.Print "  End of Life: " & WaterValues(4)

    Dim AirValues As Variant
     AirValues = environmentalImpactInfo.GetAirAcidification2
     Debug.Print " Air acidification"
     Debug.Print "  Material: " & AirValues(0)
     Debug.Print "  Use: " & AirValues(1)
     Debug.Print "  Transportation: " & AirValues(2)
     Debug.Print "  Manufacturing: " & AirValues(3)
     Debug.Print "  End of Life: " & AirValues(4)

    Dim EnergyValues As Variant
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
