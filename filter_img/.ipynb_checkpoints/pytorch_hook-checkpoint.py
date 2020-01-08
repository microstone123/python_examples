{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "class  SaveFeatures()：\n",
    "    def  __init__(self，module)：\n",
    "        self .hook = module.register_forward_hook(self .hook_fn)\n",
    "    def  hook_fn(self，module，input，output)：\n",
    "        self .features = torch.tensor(output，requires_grad = True）.cuda()\n",
    "    def  close(self)：\n",
    "        self .hook.remove()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "util_tool",
   "language": "python",
   "name": "util_tool"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
