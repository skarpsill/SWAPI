---
title: "Get and Set Routing Component Properties Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_and_Set_Routing_Component_Properties_Example_VBNET.htm"
---

# Get and Set Routing Component Properties Example (VB.NET)

This example shows how to get and set routing component properties.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Modify the path of the specified routing component.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window for the properties
 ' of the specified routing component.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.SWRoutingLib
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swRtCompMgr As RoutingComponentManager
         Dim boolstatus As Boolean
         Dim isCompTypeSavedThrRLM As Boolean
         Dim LongStatus As Long
         Dim LongWarnings As Long
         Dim cpConfig As Long
         Dim compType As Long
         Dim routeType As Long
         Dim routeTypeCustProp As Long
         Dim pipeSketch As String
         Dim compDesc As String
         Dim modelDoc As ModelDoc2
         Dim modelDocExt As ModelDocExtension

         If swApp Is Nothing Then  Exit  Sub

         LongStatus =  swApp.LoadAddIn(swApp.GetExecutablePath & "\sldrtadd.dll")
         If LongStatus <> 0 And LongStatus <> 2 Then ErrorMsg(swApp, "Cannot load Routing add-in") : GoTo LastLine

         modelDoc = swApp.OpenDoc6("public_documents\tutorial\api\straight tee inch.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", LongStatus, LongWarnings)
         modelDocExt = modelDoc.Extension

         If modelDoc Is Nothing Then ErrorMsg(swApp, "Failed to open straight tee inch.sldprt") : GoTo LastLine

         swRtCompMgr = modelDocExt.GetRoutingComponentManager
         If swRtCompMgr Is Nothing Then ErrorMsg(swApp, "Failed to set route component manager object") :  GoTo LastLine

         ' Set the description value
         swRtCompMgr.SetRoutingComponentDescription("Pipe Routing")

         ' Get the description value
         compDesc = swRtCompMgr.GetRoutingComponentDescription
         Debug.Print("Saved description: " & compDesc)

         ' Set the CPoint configuration value to not add CPoints
         swRtCompMgr.SetCPointConfiguration(2)

         ' Get the CPoint configuration value
         cpConfig = swRtCompMgr.GetCPointConfiguration
         Debug.Print("CPoint configuration as defined in swCPointConfig_e: " & cpConfig)

         ' Set the component type to tee type
         swRtCompMgr.SetComponentType(5)

         ' Get the component Type
         compType = swRtCompMgr.GetComponentType
         Debug.Print("Component type as defined in swRouteComponentTypeID_e: " & compType)

         ' Get the routing string for the pipe sketch
         pipeSketch = swRtCompMgr.GetRoutingStringValue(0)
         Debug.Print("Pipe sketch routing string: " & pipeSketch)

         ' Get the route type
         routeType = swRtCompMgr.GetComponentRouteType
         Debug.Print("Route type as defined in swComponentRouteType_e: " & routeType)
         ' Get the route type from custom property
         routeTypeCustProp = swRtCompMgr.GetComponentRouteTypeFromCustomProperty
         Debug.Print("Route type from custom property as defined in swComponentRouteType_e: " & routeTypeCustProp)

         ' See whether the component type was saved through the Route Library Manager
         isCompTypeSavedThrRLM = swRtCompMgr.GetRouteComponentTypeSetThrRLM
         Debug.Print("The component type is saved through the Route Library Manager: " & isCompTypeSavedThrRLM)

 LastLine:

         LongStatus = swAppp.UnloadAddIn(swApp.GetExecutablePath & "\sldrtadd.dll")
         If LongStatus <> 0 Then MsgBox("Unable to unload Add-in : Routing") :  GoTo LastLine

         boolstatus = swApp.CloseAllDocuments(True)
         If boolstatus = False Then ErrorMsg(swApp, "Failed to close all open documents")
         modelDoc = Nothing

     End Sub

     Sub ErrorMsg(ByVal swApp As SldWorks, ByVal Message As String)
         swApp.SendMsgToUser2(Message, 0, 0)
         swApp.RecordLine("'*** WARNING - General")
         swApp.RecordLine("'*** " & Message)
         swApp.RecordLine("")
     End Sub

     Public swApp As SldWorks

 End  Class
```
