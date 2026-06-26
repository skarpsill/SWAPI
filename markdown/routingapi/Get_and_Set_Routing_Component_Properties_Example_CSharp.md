---
title: "Get and Set Routing Component Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_and_Set_Routing_Component_Properties_Example_CSharp.htm"
---

# Get and Set Routing Component Properties Example (C#)

This example shows how to get and set routing component properties.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Modify the path of the specified routing component.
 // 2. Open an Immediate window.
 //
 // Postconditions: Inspect the Immediate window for the properties
 // of the specified routing component.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.SWRoutingLib;
 using System;
 using System.Diagnostics;
 namespace RoutingCompMgr_CSharp.csproj
 {

     partial class SolidWorksMacro
     {

         public void Main()
         {

             RoutingComponentManager swRtCompMgr = default(RoutingComponentManager);
             bool boolstatus = false;
             bool isCompTypeSavedThrRLM = false;
             int LongStatus = 0;
             int LongWarnings = 0;
             int cpConfig = 0;
             int compType = 0;
             int routeType = 0;
              int routeTypeCustProp = 0;
             string pipeSketch = null;
             string compDesc = null;
             ModelDoc2 modelDoc = default(ModelDoc2);
             ModelDocExtension modelDocExt = default(ModelDocExtension);

             if (swApp == null)
                 return;

             LongStatus = swApp.LoadAddIn(swApp.GetExecutablePath() +  "\\sldrtadd.dll");
             if (LongStatus != 0 & LongStatus != 2) { ErrorMsg(swApp,  "Cannot load Routing add-in"); goto LastLine; }

             modelDoc = swApp.OpenDoc6("public_documents\\tutorial\\api\\straight tee inch.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref LongStatus, ref LongWarnings);
             modelDocExt = modelDoc.Extension;

             if (modelDoc == null) { ErrorMsg(swApp, "Failed to open straight tee inch.sldprt");  goto LastLine; }

             swRtCompMgr = (RoutingComponentManager)modelDocExt.GetRoutingComponentManager();
             if (swRtCompMgr == null) { ErrorMsg(swApp, "Failed to set route component manager object");  goto LastLine; }

             // Set the description value
             swRtCompMgr.SetRoutingComponentDescription("Pipe Routing");

             // Get the description value
             compDesc = swRtCompMgr.GetRoutingComponentDescription();
             Debug.Print("Saved description: " + compDesc);

             // Set the CPoint configuration value to not add CPoints
             swRtCompMgr.SetCPointConfiguration(2);

             // Get the CPoint configuration value
             cpConfig = swRtCompMgr.GetCPointConfiguration();
             Debug.Print("CPoint configuration as defined in swCPointConfig_e: " + cpConfig);

             // Set the component type to tee type
             swRtCompMgr.SetComponentType(5);

             // Get the component type
             compType = swRtCompMgr.GetComponentType();
             Debug.Print("Component type as defined in swRouteComponentTypeID_e: " + compType);

             // Get the routing string for the pipe sketch
             pipeSketch = swRtCompMgr.GetRoutingStringValue(0);
             Debug.Print("Pipe sketch routing string: " + pipeSketch);

             // Get the route type
             routeType = swRtCompMgr.GetComponentRouteType();
             Debug.Print("Route type as defined in swComponentRouteType_e: " + routeType);

              // Get the route type from custom property
             routeTypeCustProp = swRtCompMgr.GetComponentRouteTypeFromCustomProperty();
             Debug.Print("Route type from custom property as defined in swComponentRouteType_e: " + routeTypeCustProp);

             // See whether tthe component type was saved through the Route Library Manager
             isCompTypeSavedThrRLM = swRtCompMgr.GetRouteComponentTypeSetThrRLM();
             Debug.Print("The component type is saved through the Route Library Manager: " + isCompTypeSavedThrRLM);

          LastLine:

             LongStatus = swApp.UnloadAddIn(swApp.GetExecutablePath() + "\\sldrtadd.dll");
             if (LongStatus != 0) { ErrorMsg(swApp,  "Unable to unload Add-in : Routing"); goto LastLine; }

             boolstatus = swApp.CloseAllDocuments(true);
             if (boolstatus == false)
                 ErrorMsg(swApp, "Failed to close all open documents");
             modelDoc = null;

         }

         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         public SldWorks swApp;

     }
 }
```
