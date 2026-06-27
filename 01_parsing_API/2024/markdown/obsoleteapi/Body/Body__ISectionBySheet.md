---
title: "Body::ISectionBySheet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__ISectionBySheet.htm"
---

# Body::ISectionBySheet

This method is obsolete and has been superseded by[Body2::ISectionBySheet](sldworksAPI.chm::/Body2/Body2__ISectionBySheet.htm).

Description

This method sections a body using a sheet.

Syntax (OLE Automation)

Not available.

Syntax
(COM)

status = Body->ISectionBySheet (
Sheet, NumMaxSections, SectionedBodies, &retval )

(Table)=========================================================

| Input: | (LPBODY) Sheet | Pointer to the sheet body used to perform the section |
| --- | --- | --- |
| Input: | (long) NumMaxSections | Maximum number of sections created |
| Input: | (LPBODY*) SectionedBodies | Pointer to an array of bodies created during the section operation |
| Output: | (long) retval | Number of bodies created during the operation |
| Return: | (HRESULT)status | S_OK if successful |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body_Object$$**$$ZAccessorByCreate$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\Body\Body__ISectionBySheet.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
