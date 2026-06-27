---
title: "Apply and Remove Texture By Display State Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Display_State_Example_CSharp.htm"
---

# Apply and Remove Texture By Display State Example (C#)

This example shows how to apply and remove texture to and from a face
by display state.

```vb
//---------------------------------------------------------------------------
 // Preconditions: Verify that the specified part and texture exist.
 //
 // Postconditions:
 // 1. Opens the part and applies texture to the selected face.
 // 2. Examine the part.
 // 3. In the IDE, click the Continue button kadov_tag{{</spaces>}}at
 //    System.Diagnostics.Debugger.Break().
 // 4. Removes the texture from the selected face.
 // 5. To verify, click the Stop Debugging button in the IDE
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}to stop execution of the macro, then click anywhere
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}in the SOLIDWORKS graphics area.
 //--------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;

 namespace SetRemoveTextureByDisplayStateFaceCSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Face2 face = default(Face2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Texture texture = default(Texture);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelView modelview = default(ModelView);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool status = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string displayState = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errors = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int warnings = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string namStr = null;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Open document and select a face
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\api\\pplate.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = (ModelDocExtension) swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}status = swModelDocExt.SelectByID2("", "FACE", -0.02341747645642, 0.03900188771217, -0.008053400767039, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}face = (Face2) swSelMgr.GetSelectedObject6(1, -1);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set texture on selected face in the
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// specified display state
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}displayState = "<Default>_Display State 1";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}namStr = "<SystemTexture>\\images\\textures\\pattern\\checker2.jpg";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}texture = (Texture) swModelDocExt.CreateTexture(namStr, 5, 45, false);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}status = face.SetTextureByDisplayState(displayState, texture);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Redraw the window view
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}modelview = (ModelView)swModel.ActiveView;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}modelview.GraphicsRedraw(null);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Examine the selected face to verify
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// that the specified texture was set
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// In the IDE, click the Continue button to resume
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// running macro
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}System.Diagnostics.Debugger.Break();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Remove texture from face by display state
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}status = swModelDocExt.SelectByID2("", "FACE", -0.02341747645642, 0.03900188771217, -0.008053400767039, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}face = (Face2)swSelMgr.GetSelectedObject6(1, -1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}status = face.RemoveTextureByDisplayState(displayState);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
