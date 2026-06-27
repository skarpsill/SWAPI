---
title: "Visual Basic .NET Standalone and Add-in Applications"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Visual_Basic_.NET_Standalone_and_Add-in_Applications.htm"
---

# Visual Basic .NET Standalone and Add-in Applications

### Standalone Applications (.exe files)

To create an instance of the SOLIDWORKS software, your project should
contain lines of code similar to the following:

Sub Main

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As SldWorks.SldWorkskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp
= New SldWorks.SldWorks()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.ExitApp

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp
= Nothing

End Sub

Additionally, you must have added[references to the SOLIDWORKS type libraries](../Overview/Type_Libraries.htm).

### Add-in Applications (.dll files)

You can create a Visual Basic .NET DLL add-in using theSOLIDWORKSVB.NET Add-in Templateincluded in
the[SOLIDWORKS API
SDK](SolidWorks_API_Getting_Started_Overview.htm). See[SOLIDWORKS VB.NET Add-in Template](../Overview/Using_SolidWorks_VB.NET_Add-In_Wizard_to_Create_VB.NET_Add-In.htm)for details.

begin!kadov{{

}}end!kadov

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955" type="application/x-oleobject" id="RelatedTopic1" style="width: 1px; height: 1px;" width="1" height="1" dtcid="1">
<param name="_Version" value="65536">
<param name="_ExtentX" value="26">
<param name="_ExtentY" value="26">
<param name="_StockProps" value="13">
<param name="ForeColor" value="0">
<param name="BackColor" value="13160660">
<param name="UseButton" value="0">
<param name="ControlLabel" value="See Also">
<param name="UseIcon" value="0">
<param name="Items" value="StandaloneApplicationsLibraries$$**$$VisualBasicStandaloneApplicationsLibraryFiles$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\HELP\Cheryle_Working_Folder\SW2010\ROBOHELP\sldworksAPIProgGuide\GettingStarted\Visual_Basic_.NET_Standalone_and_Add-in_Applications.htm">
<param name="_ID" value="RelatedTopic1">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
