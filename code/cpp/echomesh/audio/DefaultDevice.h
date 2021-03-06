#ifndef __ECHOMESH_DEFAULTDEVICE__
#define __ECHOMESH_DEFAULTDEVICE__

#include "echomesh/base/Echomesh.h"

namespace echomesh {
namespace audio {

double defaultInputSampleRate();
double defaultOutputSampleRate();
string defaultInputDevice();
string defaultOutputDevice();

unique_ptr<AudioDeviceManager> outputManager(const string& name = "",
                                             int channels = 2,
                                             double sampleRate = 0.0);

}  // namespace audio
}  // namespace echomesh

#endif  // __ECHOMESH_DEFAULTDEVICE__
