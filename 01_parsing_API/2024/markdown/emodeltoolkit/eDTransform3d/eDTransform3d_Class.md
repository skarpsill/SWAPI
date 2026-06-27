---
title: "eDTransform3d Class"
project: ""
interface: "eDTransform3d"
member: ""
kind: "class"
source: "emodeltoolkit/eDTransform3d/eDTransform3d_Class.htm"
---

# eDTransform3d Class

(Generated Script Links)========================================

(Generated Code)================================================

(WARNING: DO NOT EDIT OR DELETE THIS SECTION!)==================

begin!kadov{{===================================================

}}end!kadov=====================================================

(==============================================================)

(Table)=========================================================

| See
Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Represents a 3D transform: translation, rotation, and scale.

#### Header file code

class eDTransform3d

{

public:

eDTransform3d();

eDTransform3d( const[eDMatrix3d](../eDMatrix3d/eDMatrix3d_Class.htm)&m, const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&v, double s = 1.0, bool
rt = false, bool rf = false, bool sh = false );

eDTransform3d( const
eDTransform3d &tr );

eDTransform3d( const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&axis, double angle );
// Rotate by angle about axis

eDTransform3d( const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)&shift ); // Translate
by shift

eDTransform3d( double
scale );

const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)& translation() const;

const[eDMatrix3d](../eDMatrix3d/eDMatrix3d_Class.htm)& affine() const;

double scale_factor()
const;

void scale( double
d );

[eDPt3d](../eDPt3d/eDPt3d_Class.htm)apply_to_position( const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)& ) const;

[eDPt3d](../eDPt3d/eDPt3d_Class.htm)apply_to_unitvec( const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)& ) const;

[eDPt3d](../eDPt3d/eDPt3d_Class.htm)apply_to_vector( const[eDPt3d](../eDPt3d/eDPt3d_Class.htm)& ) const;

double apply_to_scalar(
double p ) const;

eDTransform3d inverse()
const;

eDTransform3d mult(
const eDTransform3d &t2 ) const;

bool is_shear() const;

bool is_rotate() const;

bool is_reflect() const;

bool is_identity()
const;

bool is_isomorphic()
const;

};

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Metadata type="DesignerControl" startspan
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
<param name="Items" value="MathClasses$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDTransform3d\eDTransform3d_Class.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZGeteDTransform3d$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\eModelToolkit\eDTransform3d\eDTransform3d_Class.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
