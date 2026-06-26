---
title: "ComponentStateChangeNotify - AssemblyDoc Event"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDocEvents/AssemblyDocEvents__ComponentStateChangeNotify.htm"
---

# ComponentStateChangeNotify - AssemblyDoc Event

This
event is obsolete and has been superseded by AssemblyDoc event[ComponentStateChangeNotify2](sldworksAPI.chm::/AssemblyDocEvents/AssemblyDocEvents__ComponentStateChangeNotify2.htm).

Description

This event is fired whenever the state of a
component within this assembly changes.

status = ComponentStateChangeNotify ( componentModel
, oldCompState , newCompState )

(Table)=========================================================

| Input: | (LPDISPATCH) componentModel | Pointer to the component model |
| --- | --- | --- |
| Input: | (short) oldCompState | Previous state of the component |
| Input: | (short) newCompState | New state of the component |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

SolidWorks fires this event on this AssemblyDoc
even if it is not the active document. However, SolidWorks does not generate
this notification if a part is explicitly opened by the user or opened
programmatically. In this situation, SolidWorks resolves the component
part in any open assembly that references the part. Your application must
recognize this by watching for SldWorksEvents::FileOpenNotify.

When a component is resolved or unsuppressed, its
ModelDoc object becomes available to your application. Within this notification,
you can get this object and register for other events. This might be useful
for Project Data Management (PDM) applications that want to ask the user
to check out the assembly component if the user tries to make changes.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\AssemblyDocEvents\AssemblyDocEvents__ComponentStateChangeNotify.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="AssemblyDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\AssemblyDocEvents\AssemblyDocEvents__ComponentStateChangeNotify.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
