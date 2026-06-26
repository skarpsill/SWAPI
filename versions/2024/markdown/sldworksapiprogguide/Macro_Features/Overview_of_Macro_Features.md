---
title: "Overview of Macro Features"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/Overview_of_Macro_Features.htm"
---

# Overview of Macro Features

Macro features are application-defined features that users can add to
a SOLIDWORKS model. The effect of a macro feature on the model is defined
by programs that you, or a third-party, develop.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Macro features use one of two techniques to specify their intended behavior.
They can be associated either with functions:

- contained within a SOLIDWORKS[VBA
  macro file (*.swp)](VBA_Macro_Files.htm).

  - or -
- exposed by a[COM
  server DLL or executable](Exposed_COM_DLL_or_Executable.htm).

**NOTE**: You cannot record or write macro features using SOLIDWORKS .NET
macros.

You must write macro feature functions to define your macro feature.

(Table)=========================================================

| Macro feature function | VBA | COM | Comment |
| --- | --- | --- | --- |
| Edit definition | Required | Required | Called whenever the user edits the macro feature's definition. |
| Rebuild | Required | Required | Called whenever the macro feature rebuilds. |
| Security | Optional | Required | Allows you to specify whether instances of the macro feature can be
edited, suppressed, or deleted from the model. |

The names of the VBA macro feature functions must begin withswm.
For example, you could name the functionsswmEdit,swmRebuild, andswmSecurity.

Users must be able to run the program that creates the macro feature
whenever they want to add one to a model.

The[IMacroFeatureData Interface](MacroFeatureData_Interface.htm)supports macro features.

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
<param name="Items" value="MacroFeatureInterface$$**$$VBAMacro$$**$$COMMacro$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\HELP\Cheryle_Working_Folder\SW2010\ROBOHELP\sldworksAPIProgGuide\Macro_Features\Overview_of_Macro_Features.htm">
<param name="_ID" value="RelatedTopic1">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>

metadata type="DesignerControl" endspan
