---
title: "DrSection::EnumExcludedComponents"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrSection/DrSection__EnumExcludedComponents.htm"
---

# DrSection::EnumExcludedComponents

This method is obsolete and has been superseded
by[DrSection::EumExcludedComponents2](sldworksAPI.chm::/DrSection/DrSection__EnumExcludedComponents2.htm).

Description

This method gets all of the assembly components
that are excluded from this section cut.

Syntax (OLE Automation)

See DrSection::GetExcludedComponents.

Syntax (COM)

status = DrSection->EnumExcludedComponents ( &exComps
)

(Table)=========================================================

| Output: | (LPENUMCOMPONENTS) exComps | Pointer to the EnumComponents object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The ability to exclude components from section
cuts applies only to assembly section views. For section views of parts,
this method returns NULL. To access the enumerated list of excluded components,
see the EnumComponents object.

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZGetEnumDrSections$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\DrSection\DrSection__EnumExcludedComponents.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
