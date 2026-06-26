---
title: "Get Part's Feature Statistics Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Part's_Feature_Statistics_Example_VBNET.htm"
---

# Get Part's Feature Statistics Example (VB.NET)

This example shows how to get the statistics of all of the features
in a part document.

```vb
'-------------------------------------------
 ' Preconditions:
 ' 1. Open a part that has multiple features.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Gets the statistics for the features in
 '    the part.
 ' 2. Examine the Immediate window.
 '-------------------------------------------
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeatStat As FeatureStatistics
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeatMgr As FeatureManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim featnames As Object
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim feattypes As Object
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim features As Object
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim featureUpdateTimes As Object
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim featureUpdatePercentTimes As Object
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim iter As Integer

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeatMgr = swModel.FeatureManager

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeatStat = swFeatMgr.FeatureStatistics

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeatStat.Refresh()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Model name: kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}" & swFeatStat.PartName)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Number of features: kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}" & swFeatStat.FeatureCount)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Number of solid bodies: kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}" & swFeatStat.SolidBodiesCount)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Number of surface bodies: " & swFeatStat.SurfaceBodiesCount)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Total rebuild time: kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}" & swFeatStat.TotalRebuildTime)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}featnames = swFeatStat.FeatureNames
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}feattypes = swFeatStat.FeatureTypes
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}features = swFeatStat.features
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}featureUpdateTimes = swFeatStat.featureUpdateTimes
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}featureUpdatePercentTimes = swFeatStat.FeatureUpdatePercentageTimes
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not featnames Is Nothing Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}For iter = 0 To UBound(featnames)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Feature name: kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}" & featnames(iter))
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Feature type: kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}" & feattypes(iter))
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Update time: kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}" & featureUpdateTimes(iter))
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Update % time: kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}" & featureUpdatePercentTimes(iter))
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Next iter
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

 End Class
```
