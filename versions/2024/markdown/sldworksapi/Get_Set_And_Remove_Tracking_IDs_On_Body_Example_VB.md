---
title: "Get, Set, And Remove Tracking IDs On Body (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Set_And_Remove_Tracking_IDs_On_Body_Example_VB.htm"
---

# Get, Set, And Remove Tracking IDs On Body (VBA)

This example shows how to get, set, and remove tracking IDs on a body.
Tracking IDs reliably associate application-specific data across modeling
operations.

```vb
'------------------------------------------
' Preconditions: Part document with a single part is open.
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}The selected body has not been assigned any
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}tracking IDs.
'
' Directions: kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Run the macro once, and the
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}the selected body is assigned
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}a tracking ID of 12. Run
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}the macro again, and the selected body
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}is assigned tracking ID of 16. The
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}the tracking ID is then deleted from the
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}body.
'
' Postconditions: None
'------------------------------------------
Option Explicit

Sub main()

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swApp kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}As SldWorks.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}As SldWorks.ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModelExtn kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}As ModelDocExtension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSelMgr kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}As SldWorks.SelectionMgr
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swBody kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}As SldWorks.Body2
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
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Stop ' Select body in Bodies folder
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swBody = swSelMgr.GetSelectedObject6(1, -1)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "---------------------------------"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim NbrTrackingIds As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}NbrTrackingIds = swBody.GetTrackingIDsCount(Cookies)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Body Tracking IDs:"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If (NbrTrackingIds = 0) Then
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}No tracking IDs"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Setting tracking ID..."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}SetTrackingID Result (if 0, then call successful): " & swBody.SetTrackingID(Cookies, 12)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}GetTrackingIDs Result (if 0, then call successful): " & swBody.GetTrackingIDs(Cookies, vTrackingIDs)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Tracking ID after SetTrackingID call : " & vTrackingIDs(0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End
kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tracking IDs exist..."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Getting tracking ID..."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}GetTrackingIDs Result (if 0, then call successful): " & swBody.GetTrackingIDs(Cookies, vTrackingIDs)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Tracking ID before SetTracingID call : " & vTrackingIDs(0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " "
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}SetTrackingID Result (if 0, then call successful): " & swBody.SetTrackingID(Cookies, 16)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}GetTrackingIDs Result (if 0, then call successful): " & swBody.GetTrackingIDs(Cookies, vTrackingIDs)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Tracking ID after SetTrackingID call: " & vTrackingIDs(0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " "
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Remove Tracking ID..."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}RemoveTrackingID Result (if 0, then call successful): " & swBody.RemoveTrackingID(Cookies)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}Number of tracking IDs on this body: " & swBody.GetTrackingIDsCount(Cookies)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "---------------------------------"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
End Sub
```
