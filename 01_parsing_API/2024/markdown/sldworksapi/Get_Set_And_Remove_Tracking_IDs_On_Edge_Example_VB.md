---
title: "Get, Set, And Remove Tracking IDs On Edge (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Set_And_Remove_Tracking_IDs_On_Edge_Example_VB.htm"
---

# Get, Set, And Remove Tracking IDs On Edge (VBA)

This example shows how to get, set, and remove tracking IDs on an edge.
Tracking IDs reliably associate application-specific data across modeling
operations.

```vb
'------------------------------------------
'
' Preconditions: Part document with a single part is open.
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}The selected edge on the part has not
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}been assigned any tracking IDs.
'
' Directions: kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Run the macro once, and the
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}the selected edge is assigned
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}a tracking ID of 12. Run
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}the macro again, and the selected edge
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}is assigned a tracking ID of 16. The
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}the tracking ID is then deleted from the
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}edge.
'
' Postconditions: None
'
'------------------------------------------
Option Explicit

Sub main()

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swApp kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}As SldWorks.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}As SldWorks.ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModelExtn kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}As ModelDocExtension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSelMgr kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}As SldWorks.SelectionMgr
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swEdge kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}As SldWorks.Edge
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim Cookies kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vTrackingIDs kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim TrackingID kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim bRebuild kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}As Boolean

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swApp = CreateObject("SldWorks.Application")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Cookies = swApp.RegisterTrackingDefinition("Tracking_API")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If (Cookies = -1) Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}' No valid cookies found
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Stop
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSelMgr = swModel.SelectionManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Stop ' Select and edge on the part
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swEdge = swSelMgr.GetSelectedObject6(1, -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "---------------------------------"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim NbrTrackingIds As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}NbrTrackingIds = swEdge.GetTrackingIDsCount(Cookies)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Edge Tracking IDs:"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If (NbrTrackingIds = 0) Then
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}No tracking IDs"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Setting tracking ID..."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}SetTrackingID Result (if 0, then call successful): " & swEdge.SetTrackingID(Cookies, 12)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}GetTrackingIDs Result (if 0, then call successful): " & swEdge.GetTrackingIDs(Cookies, vTrackingIDs)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Tracking ID after SetTrackingID call : " & vTrackingIDs(0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End
kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tracking IDs exist..."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Getting tracking ID..."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}GetTrackingIDs Result (if 0, then call successful): " & swEdge.GetTrackingIDs(Cookies, vTrackingIDs)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Tracking ID before SetTracingID call : " & vTrackingIDs(0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " "
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}SetTrackingID Result (if 0, then call successful): " & swEdge.SetTrackingID(Cookies, 16)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}GetTrackingIDs Result (if 0, then call successful): " & swEdge.GetTrackingIDs(Cookies, vTrackingIDs)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Tracking ID after SetTrackingID call: " & vTrackingIDs(0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " "
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Remove Tracking ID..."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}RemoveTrackingID Result (if 0, then call successful): " & swEdge.RemoveTrackingID(Cookies)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}Number of tracking IDs on this body: " & swEdge.GetTrackingIDsCount(Cookies)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "---------------------------------"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
End Sub
```
